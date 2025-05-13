import os

file_path = input('Enter File Name with extension: ')

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"'{file_path}' deleted successfully.")
else:
    print(f"'{file_path}' does not exist.")