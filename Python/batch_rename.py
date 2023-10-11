import os


def rename_files_in_directory(directory, naming_pattern):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    file_list = os.listdir(directory)
    counter = 1

    for filename in file_list:
        # Build the new filename using the specified naming pattern
        new_filename = naming_pattern.format(counter)
        counter += 1

        # Get the full paths for the old and new filenames
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)


if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    naming_pattern = input("Enter the naming pattern (use {{}} as a placeholder for numbering): ")

    rename_files_in_directory(directory, naming_pattern)
    print("Files renamed successfully.")

# Demo
#
# 1. Enter the directory path: `/path/to/your/directory`
# 2. Enter the naming pattern: `file_{}.txt`
#
# Assuming you have the following files in the directory `/path/to/your/directory`:
#
# - `document1.txt`
# - `document2.txt`
# - `document3.txt`
#
# After running the program with the sample input, the files will be renamed as follows:
#
# - `file_1.txt`
# - `file_2.txt`
# - `file_3.txt`
