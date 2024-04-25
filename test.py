import unittest
from diff import resolve_categorized_diff

class TestDiffResolution(unittest.TestCase):

    def test_interpreter_changes(self):
        snippet_a = "x = 5\n"
        snippet_b = "x = 10\n"
        expected_result = {
            'comment': [],
            'interpreter': ['-x = 5', '+x = 10'],
            'formatting': []
        }
        self.assertDictEqual(resolve_categorized_diff(snippet_a, snippet_b), expected_result)
        
    def test_formatting_changes(self):
        snippet_a = "def func():\n    return 42\n"
        snippet_b = "def func():\n\treturn 42\n"
        expected_result = {
            'comment': [],
            'interpreter': [],
            'formatting': ['-    return 42', '+\treturn 42']
        }
        self.assertDictEqual(resolve_categorized_diff(snippet_a, snippet_b), expected_result)

    def test_comment_changes(self):
        snippet_a = "# Old comment\nx = 5\n"
        snippet_b = "# New comment\nx = 5\n"
        expected_result = {
            'comment': ['-# Old comment', '+# New comment'],
            'interpreter': [],
            'formatting': []
        }
        self.assertDictEqual(resolve_categorized_diff(snippet_a, snippet_b), expected_result)
        
    def test_combined_changes(self):
        snippet_a = "# Old comment\nx = 5\n"
        snippet_b = "# New comment\nx = 10\n"
        expected_result = {
            'comment': ['-# Old comment', '+# New comment'],
            'interpreter': ['-x = 5', '+x = 10'],
            'formatting': []
        }
        self.assertDictEqual(resolve_categorized_diff(snippet_a, snippet_b), expected_result)
        
    def test_no_changes(self):
        snippet_a = "x = 5\n"
        snippet_b = "x = 5\n"
        expected_result = {
            'comment': [],
            'interpreter': [],
            'formatting': []
        }
        self.assertDictEqual(resolve_categorized_diff(snippet_a, snippet_b), expected_result)

    def test_add_remove_lines(self):
        snippet_a = "x = 5\ny = 10\n"
        snippet_b = "y = 10\nz = 15\n"
        expected_result = {
            'comment': [],
            'interpreter': ['-x = 5', '+z = 15'],
            'formatting': []
        }
        self.assertDictEqual(resolve_categorized_diff(snippet_a, snippet_b), expected_result)

if __name__ == '__main__':
    unittest.main()
