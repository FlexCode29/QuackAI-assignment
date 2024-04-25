import difflib

def compile_snippet(snippet):
    try:
        return compile(snippet, "<string>", "exec").co_code
    except SyntaxError:
        return None

def changes_compilation_result(snippet_a, modified_snippet):
    original_code = compile_snippet(snippet_a)
    modified_code = compile_snippet(modified_snippet)
    if original_code is None or modified_code is None:
        return True  # If there's a syntax error in any version, it's impactful
    return original_code != modified_code

def resolve_categorized_diff(snippet_a, snippet_b):
    lines_a = snippet_a.splitlines()
    lines_b = snippet_b.splitlines()
    diff = list(difflib.unified_diff(lines_a, lines_b, lineterm=''))
    
    categorized_diff = {"comment": [], "interpreter": [], "formatting": []}

    # Process each change detected in the unified diff
    for line in diff:
        if line.startswith(('+', '-')):
            action = line[0]
            clean_line = line[1:].strip()
            index = diff.index(line) - 3  # Adjusting for header lines in diff output

            if clean_line.startswith('#'):
                categorized_diff["comment"].append(line)
            else:
                # Attempt to create a modified version of snippet_a for comparison
                modified_snippet = list(lines_a)
                if action == '+' and (index < 0 or index >= len(modified_snippet)):
                    modified_snippet.append(clean_line)
                elif action == '-' and 0 <= index < len(modified_snippet):
                    modified_snippet.pop(index)
                elif action == '+' and 0 <= index < len(modified_snippet):
                    modified_snippet[index] = clean_line

                # Compare bytecode to determine if it's an interpreter or formatting change
                modified_snippet = "\n".join(modified_snippet)
                if changes_compilation_result(snippet_a, modified_snippet):
                    categorized_diff["interpreter"].append(line)
                else:
                    categorized_diff["formatting"].append(line)

    return categorized_diff

# Test the function with snippet A and B
snippet_a = (
    "# Router definition"
    "\napi_router = APIRouter()"
)
snippet_b = (
    "# Make sure endpoint are immune to missing trailing slashes"
    "\napi_router = APIRouter("
    "\n\tredirect_slashes=True"
    "\n)"
)

diff_ab = resolve_categorized_diff(snippet_a, snippet_b)

# Improved output formatting
print("Categorized diff between snippet A and B:")
print(diff_ab)
