import os
import unittest
from remove import removing
from unittest.mock import patch  # Used to mock user input and print statements


class TestRemovingFunction(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_directory"  # Name of the test directory
        self.test_file = "test_file.txt"  # Name of the test file
        os.makedirs(self.test_dir, exist_ok=True)  # Create the test directory
        with open(os.path.join(self.test_dir, self.test_file), 'w') as f:
            f.write("This a test file to test my removing function")  # Create a test file in the directory

    def tearDown(self):
        if os.path.exists(self.test_dir):  # Check if the directory exists
            for file in os.listdir(self.test_dir):  # Remove all files in the directory
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)  # Remove the directory itself

    def test_file_deletion(self):
        # Call the function to delete a test file
        removing(self.test_file, self.test_dir)

        # Check if the file no longer exists
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, self.test_file)))

    def test_directory_deletion(self):
        # Call the function to delete the test directory
        removing(self.test_file, self.test_dir)  # First delelte the file, then delete a directory
        removing("", self.test_dir)

        # Check if the directory no longer exists
        self.assertFalse(os.path.exists(self.test_dir))

    def test_nonexistent_file(self):
        # Call the function with non existent file to check if it works correctly
        with patch("builtins.print") as m:  # Mock the print function
            removing("nonexist_file.txt", self.test_dir)

        # Check for the message
        m.assert_called_with('The file was not found or doesn`t exist!')

    def test_nonexistent_directory(self):
        # Call the function with non existent directory to check if everything works correctly
        with patch("builtins.print") as m:
            removing("any_file.txt", "nonexistent_directory")

        m.assert_called_with("The directory was not found or doesn`t exist")


if __name__ == "__main__":
    unittest.main()
