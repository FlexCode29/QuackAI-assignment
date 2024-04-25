import difflib
snippet_a = (
    "# Router definition"
    "\napi_router = APIRouter()"
)
snippet_b = (
    "# Make sure endpoint are immune to missing trailing slashes"
    "\napi_router = APIRouter(redirect_slashes=True)"
)
snippet_c = (
    "# Router definition"
    "\napi_router = APIRouter("
    "\n\tredirect_slashes=True"
    "\n)"
)


def resolve_diff_final(snippet_a, snippet_b):
    lines_a = snippet_a.splitlines()
    lines_b = snippet_b.splitlines()

    diff = list(difflib.unified_diff(lines_a, lines_b, lineterm=''))
    meaningful_diff = []

    # Prepare to match lines
    additions = [line for line in diff if line.startswith('+ ')]
    deletions = [line for line in diff if line.startswith('- ')]

    # Match deletions with additions
    while deletions:
        deletion = deletions.pop(0)
        clean_deletion = deletion[2:].strip()
        if clean_deletion.startswith('#'):
            continue  # Skip comments in deletions

        matched = False
        for i, addition in enumerate(additions):
            clean_addition = addition[2:].strip()
            if clean_addition.startswith('#'):
                continue  # Skip comments in additions
            # Consider a match if there is any addition not just a comment
            meaningful_diff.append(f"{deletion}\n{addition}")
            del additions[i]
            matched = True
            break
        
        if not matched:
            # Append deletions that didn't find any non-comment additions
            meaningful_diff.append(deletion)

    # Append remaining additions (not matched but important)
    for addition in additions:
        clean_addition = addition[2:].strip()
        if not clean_addition.startswith('#'):
            meaningful_diff.append(addition)

    return meaningful_diff

# Running the final debugging function on the initial snippets
print("Final testing of diff between snippet A and B:")
print(resolve_diff_final(snippet_a, snippet_b))


print("Final testing of diff between snippet B and C:")
print(resolve_diff_final(snippet_b, snippet_c))