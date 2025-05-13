file_path = input('Enter File Name with extension: ')

with open(file_path, 'w') as file:
    file.write("Hello Bhavesh!\nThis is a new file created using Python.")
    print(f"Data written to '{file_path}' successfully.")