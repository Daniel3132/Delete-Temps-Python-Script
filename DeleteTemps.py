import logging
import sys

from auth.check_admin import check_admin
from delete.delete_files import delete_files
from folders.folders import folders_to_clean


# Check if script is running with elevated permissions
if not check_admin():
    print('Script is not running with elevated permissions.')
    print('Please re-run the script as an administrator.')
    print('Script aborted.')
    input('Press enter to exit...')
    sys.exit(1)

# print all folders to delete
print('This script will delete the contents of the temporary folders:')
for folder in folders_to_clean:
    print(folder)
print('\n')

# Ask for user confirmation
confirm = input('Do you want to continue? (y/n)\n')
if confirm.lower() == 'y':
    try:
        # Delete files in temporary folders
        print('\nDeleting temporary files...')
        total_count = 0
        total_size = 0
        # Loop through folders and clean each one
        for folder in folders_to_clean:
            count, size = delete_files(folder)
            total_count += count
            total_size += size
        total_size /= 1000000000  # convert from b to mb
        formatted_number = "{:.1f}".format(total_size)  # left just one decimal
        print('Temporary files deleted successfully.')
        print('Deleted', total_count, 'files, freeing up',
              formatted_number, 'MBs of disk space.')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        input('Press enter to exit...')
else:
    print('Script aborted.')
    input('Press enter to exit...')

input('Press enter to exit...')
