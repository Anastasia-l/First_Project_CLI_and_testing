import os


def removing(filename, directory_name):
    if not os.path.isdir(directory_name):
        print("The directory was not found or doesn`t exist")
        return  # Exit the function early if the directory doesn`t exist`

    full_file_path = os.path.join(directory_name, filename)

    # Check if the file exists
    if filename:  # Only check for files if filename is provided
        if os.path.isfile(full_file_path):
            try:
                os.remove(full_file_path)
                print(f"The file {filename} was successfully deleted from the directory")
            except FileNotFoundError:
                print(f"The file {filename} was not found")
        else:
            print("The file was not found or doesn`t exist!")
    else:
        # If there`s no filename provided attempt to delete a directory
        try:
            os.rmdir(directory_name)
            print(f"The directory {directory_name} was successfully deleted!")
        except:
            print("The directory was not discovered or some error!")
