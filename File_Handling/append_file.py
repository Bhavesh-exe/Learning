file_path = input('Enter File Name with extension: ')

with open(file_path, 'a') as file:
    file.write("\nAppending a new line to the file.")
    print(f"Data appended to '{file_path}' successfully.")