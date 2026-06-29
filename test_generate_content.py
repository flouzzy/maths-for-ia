import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
import generate_content

import os

class TestIsSafePath(unittest.TestCase):

    def test_safe_paths(self):
        base = "/var/www/html"
        # File directly inside base
        self.assertTrue(generate_content.is_safe_path(base, "/var/www/html/index.html"))
        # File in subdirectory
        self.assertTrue(generate_content.is_safe_path(base, "/var/www/html/assets/style.css"))
        # The base directory itself
        self.assertTrue(generate_content.is_safe_path(base, "/var/www/html"))
        # Path traversal that resolves back inside base
        self.assertTrue(generate_content.is_safe_path(base, "/var/www/html/assets/../index.html"))

    def test_unsafe_paths(self):
        base = "/var/www/html"
        # Completely outside base
        self.assertFalse(generate_content.is_safe_path(base, "/var/log/apache2/error.log"))
        # Path traversal escaping base
        self.assertFalse(generate_content.is_safe_path(base, "/var/www/html/../../etc/passwd"))
        # Absolute path outside base
        self.assertFalse(generate_content.is_safe_path(base, "/etc/passwd"))

    def test_sibling_directory_prefix(self):
        # Tests prevention of prefix bypass vulnerabilities (CWE-22)
        # e.g., string prefix check might allow "/var/www/html_backup"
        base = "/var/www/html"
        self.assertFalse(generate_content.is_safe_path(base, "/var/www/html_backup/data.txt"))

    def test_relative_paths(self):
        # Uses the current working directory implicitly via abspath
        base = "my_safe_dir"
        path_inside = os.path.join("my_safe_dir", "file.txt")
        path_outside = os.path.join("..", "other_dir", "file.txt")
        self.assertTrue(generate_content.is_safe_path(base, path_inside))
        self.assertFalse(generate_content.is_safe_path(base, path_outside))

class TestGenerateContent(unittest.TestCase):

    @patch('sys.argv', ['generate_content.py', 'prompt.txt'])
    @patch('sys.stdout', new_callable=MagicMock)
    def test_main_insufficient_args(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            generate_content.main()
        self.assertEqual(cm.exception.code, 1)

    @patch('sys.argv', ['generate_content.py', 'prompt.txt', 'output.txt'])
    @patch('builtins.open', new_callable=mock_open, read_data='Test prompt')
    @patch('generate_content.genai.Client')
    def test_main_success(self, mock_client_class, mock_file):
        # Setup mock client and response
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_response = MagicMock()
        mock_response.text = 'Test response'
        mock_client.models.generate_content.return_value = mock_response

        # Call main
        generate_content.main()

        # Assert file opens
        mock_file.assert_any_call('prompt.txt', 'r', encoding='utf-8')
        mock_file.assert_any_call('output.txt', 'w', encoding='utf-8')

        # Assert genai was called
        mock_client.models.generate_content.assert_called_once_with(
            model='gemini-2.5-pro',
            contents='Test prompt'
        )

        # Assert file write
        handle = mock_file()
        handle.write.assert_called_once_with('Test response')

if __name__ == '__main__':
    unittest.main()
