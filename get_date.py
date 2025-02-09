import os
from datetime import datetime

use_recursive = True


def get_file_birthday(full_path):
    timestamp = os.path.getctime(full_path)
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def rename_file_with_date(full_path):
    base_name, extension = os.path.splitext(os.path.basename(full_path))
    parent_folder = os.path.dirname(full_path)

    new_name = f"{base_name}_{get_file_birthday(full_path)}{extension}"
    new_full_path = os.path.join(parent_folder, new_name)

    os.rename(full_path, new_full_path)
    print(f"Renamed: {os.path.basename(full_path)} -> {new_name}")


def process_folder(folder_path, recursive=False):
    if recursive:
        for root, _, files in os.walk(folder_path):
            for file in files:
                rename_file_with_date(os.path.join(root, file))
    else:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                rename_file_with_date(item_path)

    if __name__ == "__main__":
        target_folder = input("Enter directory: ")
        if not os.path.exists(target_folder):
            print("Error, folder doesn`t exist!")
        else:
            confirm = input("This will rename files! Type 'YES' to continue: ")
            if confirm.lower() == "YES".lower():
                process_folder(target_folder, use_recursive)
            else:
                print("Cancelled by user")
