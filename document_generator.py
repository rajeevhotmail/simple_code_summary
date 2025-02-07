import os
class DocumentationGenerator:
    def __init__(self):
        self.doc_file = "project_documentation.md"

    def generate_docs(self, analysis_results, call_stacks):
        with open(self.doc_file, "w") as f:
            # Project Header with badges
            f.write("# Project Analysis Report\n\n")
            f.write("![Python](https://img.shields.io/badge/python-3.6%2B-blue)\n\n")

            # Table of Contents
            f.write("## Contents\n")
            f.write("1. [Overview](#overview)\n")
            f.write("2. [Function Relationships](#function-relationships)\n")
            f.write("3. [Code Analysis](#code-analysis)\n\n")

            # Overview Section
            f.write("## Overview\n")
            f.write(f"Total files analyzed: {len(analysis_results)}\n\n")


            # Function Relationships Section
            f.write("## Function Relationships\n\n")
            self.generate_function_relationships(f, analysis_results)
            # Add our new mermaid diagram
            self.generate_mermaid_diagram(f, call_stacks)
            for file_result in analysis_results:
                for function in file_result['functions']:
                    f.write(f"### `{function['name']}`\n")
                    f.write(f"**Location**: `{os.path.basename(file_result['file'])}`\n\n")
                    f.write("<details>\n<summary>Dependencies</summary>\n\n")
                    f.write("#### Calls:\n")
                    if function['relationships']['calls']:
                        for call in function['relationships']['calls']:
                            f.write(f"- `{call}`\n")
                    else:
                        f.write("- No outgoing calls\n")

                    f.write("\n#### Called By:\n")
                    if function['relationships']['called_by']:
                        for caller in function['relationships']['called_by']:
                            f.write(f"- `{caller}`\n")
                    else:
                        f.write("- No incoming calls\n")
                    f.write("</details>\n\n")

                    # Function Analysis
                    f.write("#### Analysis\n")
                    f.write(f"```python\n{function.get('operations', 'No operations detected')}\n```\n\n")
                    f.write("---\n\n")  # Section separator

            # Code Analysis Section
            f.write("## Code Analysis\n\n")
            for file_result in analysis_results:
                f.write(f"### {os.path.basename(file_result['file'])}\n")
                f.write("```python\n")
                f.write(f"# File: {file_result['file']}\n")
                f.write(f"{file_result.get('description', 'No description available')}\n")
                f.write("```\n\n")

            f.write("## Function Call Stacks\n\n")
            for entry_point, stack in call_stacks.items():
                f.write(f"### Entry Point: `{entry_point}`\n\n")
                f.write("```mermaid\nflowchart TD\n")
                for func in stack:
                    indent = "  " * func['depth']
                    func_id = f"{func['name']}[{func['name']}]"
                    for called in func['calls']:
                        f.write(f"{indent}{func_id} --> {called}[{called}]\n")
                f.write("```\n\n")

    def generate_function_relationships(self, f, analysis_results):
        for file_result in analysis_results:
            f.write(f"### File: `{os.path.basename(file_result['file'])}`\n\n")
            for function in file_result['functions']:
                # Function name and signature
                f.write(f"#### Function: `{function['name']}`\n")
                if 'signature' in function:
                    params = ', '.join(function['signature'].get('parameters', []))
                    f.write(f"**Signature:** `def {function['name']}({params})`\n\n")

                # Operations
                f.write(f"**Operations:**\n```python\n{function['operations']}\n```\n\n")

                # Dependencies
                f.write("**Dependencies:**\n")
                f.write("- Calls: " + (', '.join(f'`{c}`' for c in function['relationships']['calls']) or 'None') + "\n")
                f.write("- Called by: " + (', '.join(f'`{c}`' for c in function['relationships']['called_by']) or 'None') + "\n\n")
                f.write("---\n\n")

    def generate_mermaid_diagram(self, f, call_stacks):
        f.write("\n## Call Stack Visualization\n\n")
        f.write("```mermaid\nflowchart TD\n")

        for entry_point, stack in call_stacks.items():
            for func in stack:
                for called in func['calls']:
                    f.write(f"    {func['name']}[{func['name']}] --> {called}[{called}]\n")

        f.write("```\n\n")