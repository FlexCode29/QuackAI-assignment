# QuackAI-assignment

# Code Diff Resolver

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

## Usage

To use the Code Diff Resolver, first ensure that `diff.py` is located in the main folder of your project. Then, simply import and call the `resolve_categorized_diff` function from your Python script, passing in two code snippets you wish to compare.

Example usage:

```python
from diff import resolve_categorized_diff

snippet_a = "x = 5\n"
snippet_b = "x = 10\n"

resolved_diffs = resolve_categorized_diff(snippet_a, snippet_b)
print(resolved_diffs)
```

The output will be a dictionary that categorizes changes into `comment`, `interpreter`, and `formatting`.

## Tests

A suite of unit tests is provided to ensure the functionality of the Code Diff Resolver. These tests can be run using the following command:

```bash
python -m unittest
```

Tests cover different scenarios including changes in interpreter behavior, comments, formatting, and much more.

## Credits

- `difflib`: Python standard library module used for diff resolution.
- OpenAI's ChatGPT: Provided guidance for documentation and explanation.

## Report on Code Diff Resolver Functioning

### Code Structure

The `resolve_categorized_diff` function compares two Python code snippets and categorizes the differences. The steps performed by this function are:

1. **Compilation**: Each code snippet is compiled to check its validity.
2. **Removal of Comments and Blank Lines**: Unnecessary lines are removed to focus on executable code.
3. **Bytecode Comparison**: Compares the bytecode of the snippets to determine if a change impacts the interpreter.
4. **Line-by-Line Analysis**: Each line is analyzed, and differences categorized into `comment`, `interpreter`, or `formatting`.

### Algorithm Walkthrough

- **Compilation Test**: Each snippet is compiled into bytecode. This step validates the code and prepares it for comparison.
  
- **Preprocessing**: Comments and whitespace are not relevant to interpreter behavior. These are stripped away to focus on the syntax that Python executes.

- **Resolved Diff Generation**: 
  - By applying the unified diff algorithm provided by `difflib`, the function compares the preprocessed snippets line by line and identifies the changed lines.
  - If a line only contains a comment or is empty, it’s considered a `comment` change.
  - For other lines, the code checks whether modifying the line alters the bytecode. If it does, it’s an `interpreter` change. If not, it's a `formatting` change.

### Example Walkthrough

Given two snippets `snippet_a` and `snippet_b`:

```python
snippet_a = "x = 5\n"
snippet_b = "x = 10\n"
```

Running `resolve_categorized_diff(snippet_a, snippet_b)` produces:

```json
{
    "comment": [],
    "interpreter": ["-x = 5", "+x = 10"],
    "formatting": []
}
```

This output categorically indicates that changing `x = 5` to `x = 10` is an interpreter-related change since it affects the executed bytecode.

## Conclusion

By distinguishing between different types of changes, the Code Diff Resolver can help engineers, reviewers, and automated processes to understand the implications of code modifications. It provides a language-specific context to diffs, facilitating better code review and management practices.
```

**Note:** This README assumes that the code and tests are included in a file named `diff.py`. Instructions for running the code and unit tests are given accordingly. The repository structure, installation, and usage instructions are provided to ease the setup and application of this tool without the necessity for machine learning models or complex dependencies.