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
