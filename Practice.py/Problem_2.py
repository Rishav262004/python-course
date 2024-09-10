import os

def print_directory_contents(directory):
    try:
        # List all files and directories in the given directory
        contents = os.listdir(directory)
        print(f"Contents of directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")

# Specify the directory you want to list
directory_path = '.'  # Current directory
print_directory_contents(directory_path)
