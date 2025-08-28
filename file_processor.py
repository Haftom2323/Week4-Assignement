def process_file(source_file, destination_file):
    """
    Reads content from source_file, processes it, and writes to destination_file.
    In this example, converts text to uppercase as a simple transformation.
    """
    try:
        # Read from source file
        with open(source_file, 'r') as file:
            content = file.read()
        
        # Process content (example: convert to uppercase)
        processed_content = content.upper()
        
        # Write to destination file
        with open(destination_file, 'w') as file:
            file.write(processed_content)
            
        return True, "File processed successfully!"
        
    except FileNotFoundError:
        return False, f"Error: The file '{source_file}' was not found."
    except PermissionError:
        return False, f"Error: Permission denied when accessing '{source_file}'."
    except IOError as e:
        return False, f"I/O error occurred: {str(e)}"
    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"

def main():
    print("=== File Processing Utility ===")
    print("This program reads a file, processes its content, "
          "and writes the result to a new file.\n")
    
    while True:
        source = input("Enter the source filename (or 'quit' to exit): ").strip()
        if source.lower() == 'quit':
            break
            
        destination = input("Enter the destination filename: ").strip()
        
        if not source or not destination:
            print("Error: Both filenames are required.\n")
            continue
            
        success, message = process_file(source, destination)
        print(message)
        
        if success:
            print(f"Check '{destination}' for the modified content.\n")
        else:
            print("Please try again.\n")

if __name__ == "__main__":
    main()
