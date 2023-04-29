import logging
import os
import shutil


def delete_files(folder_path):
    count = 0
    size = 0
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size += os.path.getsize(file_path)
                os.remove(file_path) # delete file
                print(file_path)
                count += 1
            except PermissionError as e:
                logging.warning(f"Unable to delete file {file_path}: {e}")
            except FileNotFoundError as e:
                logging.warning(f"File {file_path} not found: {e}")
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path) # delete dir
                count += 1
            except OSError as e:
                logging.warning(f"Unable to delete directory {dir_path}: {e}")
                try:
                    shutil.rmtree(dir_path) # delete dir
                    count += 1
                except Exception as e:
                    logging.warning(
                        f"Unable to delete directory {dir_path}: {e}")
    return count, size
