import argparse
from document_generator import DocumentationGenerator
from tree_sitter import Language, Parser
import os
import glob
from code_reader import CodeReader

class CodeAnalyzer:
    def __init__(self):  # Remove directory_path parameter
        self.parser, self.language = self.setup_parser()

    def setup_parser(self):
        LANGUAGE_PATH = os.path.expanduser('~/.tree-sitter/tree-sitter-python.so')
        language = Language(LANGUAGE_PATH, 'python')
        parser = Parser()
        parser.set_language(language)
        return parser, language

    def extract_docstring(self, node, default_description):
        # Look for docstring in the first statement of function body
        body_node = None
        for child in node.children:
            if child.type == 'block':
                body_node = child
                break

        if body_node and body_node.children:
            first_stmt = body_node.children[0]
            if first_stmt.type == 'expression_statement':
                string_node = first_stmt.children[0]
                if string_node.type == 'string':
                    return string_node.text.decode('utf8').strip('"""').strip("'''").strip()

        return default_description


    def analyze_file(self, file_path: str):
        with open(file_path, 'r') as f:
            code = f.read()
        tree = self.parser.parse(bytes(code, "utf8"))

        module_name = os.path.basename(file_path)
        default_module_desc = f"Python module for {module_name.replace('.py', '')}"
        module_doc = self.extract_docstring(tree.root_node, default_module_desc)

        function_query = self.language.query("""
            (function_definition 
                name: (identifier) @function.name
                body: (block) @function.body)
        """)

        functions = []
        captures = function_query.captures(tree.root_node)

        for node, capture_name in captures:
            if capture_name == 'function.name':
                function_name = node.text.decode('utf8')
                docstring = self.extract_docstring(node.parent, "")
                operations = self.analyze_operations(node.parent)
                operations_desc = self.generate_accurate_description(function_name, operations)

                functions.append({
                    'name': function_name,
                    'docstring': docstring,
                    'operations': operations_desc,
                    'calls': self.find_function_calls(node.parent)
                })

        return {
            'file': file_path,
            'description': module_doc,
            'functions': functions
        }

    def analyze_operations(self, node):
        operation_patterns = {
            'sorting': {'pattern': '(call function: (identifier) @sort)',
                       'description': 'Performs sequence sorting'},
            'arithmetic': {'pattern': '(binary_operator) @math',
                          'description': 'Handles mathematical calculations'},
            'json': {'pattern': '(call function: (attribute object: (identifier)) @json)',
                    'description': 'Processes API responses and JSON data'},
            'list_ops': {'pattern': '(call function: (identifier) @list)',
                        'description': 'Manages list operations'},
            'string_ops': {'pattern': '(call function: (identifier) @str)',
                          'description': 'Handles text processing'},
            'error_handling': {'pattern': '(raise_statement) @error',
                             'description': 'Implements error handling'},
            'url_handling': {'pattern': '(call function: (attribute object: (identifier)) @url)',
                            'description': 'Manages URL operations'},
            'validation': {'pattern': '(call function: (identifier) @validate)',
                          'description': 'Validates input parameters'}
        }

        detected_ops = []
        for op_type, op_info in operation_patterns.items():
            query = self.language.query(op_info['pattern'])
            if query.captures(node):
                detected_ops.append(op_info['description'])

        return " and ".join(detected_ops) if detected_ops else "Basic function operations"


    def analyze_call_stack(self, entry_point, results):
        call_stack = []
        visited = set()

        def build_call_chain(function_name, depth=0):
            if function_name in visited:
                return
            visited.add(function_name)

            # Find all function details from our analysis results
            for file_result in results:
                for func in file_result['functions']:
                    if func['name'] == function_name:
                        call_stack.append({
                            'name': function_name,
                            'depth': depth,
                            'file': file_result['file'],
                            'calls': func['calls']
                        })
                        # Recursively analyze each function call
                        for called_func in func['calls']:
                            build_call_chain(called_func, depth + 1)

        build_call_chain(entry_point)
        return call_stack



    def generate_accurate_description(self, function_name, operations_desc):
        return f"Function {function_name} {operations_desc}"

    def find_function_calls(self, node):
        query = self.language.query("""
            (call function: (identifier) @call)
        """)
        calls = set()
        for n, _ in query.captures(node):
            calls.add(n.text.decode('utf8'))
        return calls
    def map_function_relationships(self, analysis_results):
        relationships = {}

        for file_result in analysis_results:
            for function in file_result['functions']:
                function_id = f"{file_result['file']}:{function['name']}"
                relationships[function_id] = {
                    'calls': function['calls'],
                    'called_by': set(),
                    'shares_data_with': set(),
                    'module': file_result['file']
                }

        # Build called_by relationships
        for func_id, data in relationships.items():
            for called_func in data['calls']:
                for target_id in relationships:
                    if called_func in target_id:
                        relationships[target_id]['called_by'].add(func_id)

        return relationships
    def analyze_directory(self, python_files):
        results = []
        for file in python_files:
            results.append(self.analyze_file(file))

        # Generate function relationships
        relationships = self.map_function_relationships(results)

        # Add relationships to results
        for file_result in results:
            for function in file_result['functions']:
                function_id = f"{file_result['file']}:{function['name']}"
                function['relationships'] = relationships[function_id]

        return results


    def detect_entry_points(self, analysis_results):
        entry_points = set()
        main_patterns = ['send_', 'process_', 'handle_', 'main', 'run']

        for file_result in analysis_results:
            if 'main' in file_result['file'] or 'core' in file_result['file']:
                for function in file_result['functions']:
                    entry_points.add(function['name'])
            else:
                for function in file_result['functions']:
                    if any(function['name'].startswith(pattern) for pattern in main_patterns):
                        entry_points.add(function['name'])

        return list(entry_points)




def main():
    parser = argparse.ArgumentParser(description='Analyze Python code')
    parser.add_argument('--project-dir', help='Path to the project directory')
    parser.add_argument('--github-url', help='GitHub repository URL')
    args = parser.parse_args()

    reader = CodeReader()
    python_files = reader.read_from_directory(args.project_dir) if args.project_dir else reader.read_from_github(args.github_url)

    analyzer = CodeAnalyzer()
    results = analyzer.analyze_directory(python_files)

    # Use dynamic entry point detection
    entry_points = analyzer.detect_entry_points(results)
    call_stacks = {}

    print("\nFunction Call Stacks:")
    print("====================")
    for entry_point in entry_points:
        call_stack = analyzer.analyze_call_stack(entry_point, results)
        call_stacks[entry_point] = call_stack
        print(f"\nExecution path for {entry_point}:")
        for func in call_stack:
            indent = "  " * func['depth']
            print(f"{indent}-> {func['name']} (in {os.path.basename(func['file'])})")
            if func['calls']:
                print(f"{indent}   Makes calls to: {', '.join(func['calls'])}")

    doc_generator = DocumentationGenerator()
    doc_generator.generate_docs(results, call_stacks)
    print(f"\nDocumentation generated: {doc_generator.doc_file}")



if __name__ == "__main__":
    main()
