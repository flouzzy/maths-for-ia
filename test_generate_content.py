import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
import generate_content

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
