import os
import shutil


def copy_file(filename, directory_name):
    full_file_path = os.path.join(directory_name, filename)
    destination_path = input("Where to copy the file to? ")

    if os.path.isfile(full_file_path):
        try:
            shutil.copy2(full_file_path, destination_path)
            print(f"The file {filename} was successfully copied! Check that out!")
        except:
            print(f"Error copying the file {filename}")

    else:
        print(f"The file {filename} could not be found!")
