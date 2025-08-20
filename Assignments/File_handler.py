file_name = input("Enter the file name: ").strip()
def modify_content(content):
        return content.upper()

def main():
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            original_content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        exit(1)
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")
        exit(1)

    modified_content = modify_content(original_content)
    new_file_name = input("Enter the new file name to save the modified content: ").strip()

    try:
        with open(new_file_name, "w", encoding="utf-8") as f:
            f.write(modified_content)
        print(f"Modified content saved to '{new_file_name}'.")
    except IOError:
        print(f"Error: Could not write to the file '{new_file_name}'.")
        exit(1)

if __name__== "__main__":
    main()