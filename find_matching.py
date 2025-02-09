import re
import os


def find_matching_files(directory, pattern):
    print(f"Compiling regex pattern: {pattern}")
    regex = re.compile(pattern, re.IGNORECASE)
    matches = []

    try:
        print(f"Searching in directory: {directory}")
        print(f"Using pattern {pattern}")

        for root, _, files in os.walk(directory):
            print(f"Checking directory {root}")
            for file in files:
                full_path = os.path.join(root, file)
                print(f"Checking file: {full_path}")
                if regex.search(file):
                    print(f"Match found! It`s {file}")
                    matches.append(full_path)
                else:
                    print(f"No match {file}")
    except Exception as e:
        print(f"Error while searching {e}")

    return matches
