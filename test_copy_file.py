import unittest
from unittest.mock import patch
from copy import copy_file


class TestCopyFile(unittest.TestCase):
    @patch('builtins.input', return_value='/mock/directory')
    @patch('os.path.isfile')
    @patch('shutil.copy2')
    def test_copy_file_success(self, mock_copy2, mock_isfile, mock_input):
        # Simulate the file exists
        mock_isfile.return_value = True

        # Call the function
        copy_file('test_file.txt', '/mock/directory')

        # Check if os.path.isfile was called with the correct path
        mock_isfile.assert_called_with('/mock/directory\\test_file.txt')

        # Check if shulil.copy2 was called with the correct paths
        mock_copy2.assert_called_with('/mock/directory\\test_file.txt', '/mock/directory')

        # Check if the input is the destination path
        mock_input.assert_called_with("Where to copy the file to? ")


if __name__ == "__main__":
    unittest.main()
