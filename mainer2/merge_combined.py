# Function to append one text file to the bottom of another
def append_text_files(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            source_content = source.read()

        with open(destination_file, 'a') as destination:
            destination.write(source_content)

        print(f"Appended contents of '{source_file}' to '{destination_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
#source_file = 'source.txt'  # Replace with the path to your source file
#destination_file = 'destination.txt'  # Replace with the path to your destination file

#append_text_files(source_file, destination_file)