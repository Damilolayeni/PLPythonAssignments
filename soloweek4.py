file = input("Enter the filename to read: ")
try:
    with open(file, 'r') as infile:
        content = infile.read()
        modified_content = content.upper()
        new_file = f"modified_{file}"
        with open(new_file, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified file written to {new_file}")
except FileNotFoundError:
    print("Error: File does not exist.")
except IOError:
    print("Error: Could not read the file.")
