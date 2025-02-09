import os


def counting_files(directory_name):
    count = 0
    for root, dirs, files in os.walk(directory_name):
        count += len(files)
    print(count)
