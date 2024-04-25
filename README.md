# QuackAI-assignment


## Introduction

The Code Diff Resolver is a tool designed to meaningfully compare Python source code snippets and identify differences that impact the behavior of the Python interpreter. This tool enhances the standard diff resolution by categorizing differences into three types: interpreter-related changes, formatting adjustments, and comments modifications.

## Features

- **Functional Python approach:** The resolver is written as a functional Python tool without any ML dependencies or complexities.
- **Categorized diff output:** Differences are returned categorized as interpreter changes, formatting changes, or comments.
- **Python-specific analysis:** Only differences affecting the Python interpreter's execution are considered relevant and reported, ignoring pure formatting and comment changes.

## Requirements

Python 3.8 or higher is required to run this tool.

## Installation

Clone the repository and make sure Python 3.8+ is installed on your system. There are no external Python package requirements for this tool.

## Tests

A suite of unit tests is provided to ensure the functionality of the Code Diff Resolver. These tests can be run using the following command:

```bash
python -m unittest
```

### Test Scenarios

Below we detail the tests included in the suite:

#### Interpreter Changes
Tests the resolver's ability to detect changes that affect the execution:

```python
snippet_a = "x = 5\n"
snippet_b = "x = 10\n"
# Expected: Modification in variable assignment (interpreter change).
```

#### Formatting Changes
Tests detection of changes in whitespace that don't affect interpreter execution:

```python
snippet_a = "def func():\n    return 42\n"
snippet_b = "def func():\n\treturn 42\n"
# Expected: Alteration in indentation (formatting change).
```

#### Comment Changes
Evaluates how the resolver perceives modifications in comments:

```python
snippet_a = "# Old comment\nx = 5\n"
snippet_b = "# New comment\nx = 5\n"
# Expected: Changes in comment content (comment change).
```

#### Combined Changes
Measures the capability to categorize a combination of changes:

```python
snippet_a = "# Old comment\nx = 5\n"
snippet_b = "# New comment\nx = 10\n"
# Expected: Changes in both comments and executable code.
```

#### No Changes
Confirms that the resolver reports no changes when two snippets are identical:

```python
snippet_a = "x = 5\n"
snippet_b = "x = 5\n"
# Expected: No differences detected.
```

#### Add or Remove Lines
Verifies correct detection when lines are added or removed:

```python
snippet_a = "x = 5\ny = 10\n"
snippet_b = "y = 10\nz = 15\n"
# Expected: Line removal and addition (interpreter changes).
```

### Code Structure

The `resolve_categorized_diff` function compares two Python code snippets and categorizes the differences. The steps performed by this function are:

1. **Compilation**: Each code snippet is compiled to check its validity.
2. **Removal of Comments and Blank Lines**: Unnecessary lines are removed to focus on executable code.
3. **Bytecode Comparison**: Compares the bytecode of the snippets to determine if a change impacts the interpreter.
4. **Line-by-Line Analysis**: Each line is analyzed, and differences categorized into `comment`, `interpreter`, or `formatting`.