import os
from file_manager_project import counting_files
import unittest
from unittest.mock import patch


class TestCountingFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.test_dir):  # Check if the directory exists
            for root, dirs, files in os.walk(self.test_dir):
                for file in files:
                    os.remove(os.path.join(root, file))  # Removing all files
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))  # Remove all subdirectories
            os.rmdir(self.test_dir)  # Remove the main directory

    def test_empty_directory(self):  # Tests if the function counts files correctly in an empty directory
        with patch('builtins.print') as m:
            counting_files(self.test_dir)
            m.assert_called_with(0)

    def test_directory_with_files(self):
        # Create some files in the directory
        with open(os.path.join(self.test_dir, "file_1.txt"), "w") as f:
            f.write("This is file 1")
        with open(os.path.join(self.test_dir, "file_2.txt"), "w") as f:
            f.write("This is file 2")

        with patch('builtins.print') as m:
            counting_files(self.test_dir)
            m.assert_called_with(2)

    def test_directory_with_subdirectories_and_files(self):
        sub_dir = os.path.join(self.test_dir, "sub_directory")
        os.makedirs(sub_dir, exist_ok=True)

        with open(os.path.join(self.test_dir, "file1.txt"), "w") as f:
            f.write("This is file 1")
        with open(os.path.join(self.test_dir, "file2.txt"), "w") as f:
            f.write("This is file 2")
        with open(os.path.join(self.test_dir, "file3.txt"), "w") as f:
            f.write("This is file 3")

        with patch("builtins.print") as m:
            counting_files(self.test_dir)

        m.assert_called_with(3)

    def test_nonexistent_directory(self):
        non_existent_directory = "non_existent_dir"

        with patch("builtins.print") as m:
            counting_files(non_existent_directory)

        m.assert_called_with(0)


if __name__ == "__main__":
    unittest.main()
