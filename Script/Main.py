import shutil
import os

def move_file(source_file, destination_path):
    try:
        # Check if steam exists
        if not os.path.isfile(source_file):
            raise FileNotFoundError(f"The source file does not exist: {source_file}")

        # Move the startup video, replacing any existing startup at the destination
        shutil.copy(source_file, destination_path)
        print(f"File moved successfully from {source_file} to {destination_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


def read_text(text_file):
    try:
        with open(text_file, 'r') as file:
            # Read the contents of the file
            file_path_to_move = file.read().strip()  # Read the file path and remove any leading/trailing whitespace
        print("File path read successfully.")

        # Construct the destination path
        destination_file = os.path.join(destination_dir, os.path.basename(file_path_to_move))

        # calls the move function to move the video
        move_file(file_path_to_move, destination_file)
    except FileNotFoundError:
        print(f"The file {text_file} was not found.")
    except IOError:
        print(f"An error occurred while reading the file {text_file}.")


# Use raw strings to handle backslashes in paths
#Steamui is for the bigpicture startup thats where they keep the movies
destination_dir = r'C:\Program Files (x86)\Steam\steamui\movies'
text_location = r'C:\Users\YOUR_USER\Documents\SStarty\location.txt'

# Ensure destination directory exists
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Read the file path from the text file and move the file
read_text(text_location)
quit()
