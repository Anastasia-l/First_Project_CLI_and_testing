import unittest
import os
import re
import tempfile
import shutil
from file_manager_project import find_matching_files


class TestFindMatchingFiles(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()  # Create a temporary directory

        # Create some test files
        self.files = {
            'test1.txt': "Test file N1",
            'test2.doc': "Test file N2",
            'test3.txt': "Test file N3",
            'image.png': "Test file N4"
        }

        for filename, content in self.files.items():
            with open(os.path.join(self.test_dir, filename), "w") as f:
                f.write(content)

    def tearDown(self):
        shutil.rmtree(self.test_dir)  # Remove the temporary directory after the test

    def test_finding_matching_files(self):
        pattern = r'\.txt$'
        result = find_matching_files(self.test_dir, pattern)

        expected = [
            os.path.join(self.test_dir, 'test1.txt'),
            os.path.join(self.test_dir, 'test3.txt')
        ]

        self.assertEqual(sorted(result), sorted(expected))

    def test_find_mathincg_no_match(self):
        pattern = r'\.pdf'
        result = find_matching_files(self.test_dir, pattern)

        # Assert that there are no matching files
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
