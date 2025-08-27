'''
PROBLEM STATEMENT:
Create a Python script that automatically organizes files in a folder by file type - 
putting images, documents, and other files into separate subfolders.
'''

import os      # Module for interacting with the operating system
import shutil  # Module for moving and copying files

def organize_files(folder_path):
    # Define file types and their associated extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css', '.java']
    }

    # Loop through every item in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Proceed only if it's a file (not a folder)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)  # Split the filename and extension
            ext = ext.lower()  # Convert extension to lowercase for consistent matching
            moved = False      # Track whether the file has been moved

            # Check which file type category the file belongs to
            for folder, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(folder_path, folder)  # Destination folder path
                    moved = True
                    break  # Exit loop once match is found

            # If the file doesn't match any known type, move it to 'Others'
            if not moved:
                dest_folder = os.path.join(folder_path, 'Others')       

            # Create the destination folder if it doesn't exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            # Move the file to the destination folder
            shutil.move(file_path, os.path.join(dest_folder, file_name))    
            print(f'Moved: {file_name} to {dest_folder}')  # Print status update

# Only run this part if the script is executed directly (not imported)
if __name__ == "__main__":
    # Ask the user for the path to the folder they want to organize
    folder_to_organize = input("Enter the path of the folder to organize: ").strip()

    # Check if the path is a valid directory
    if os.path.isdir(folder_to_organize):
        organize_files(folder_to_organize)  # Run the file organizer
    else:
        # Error message if the path is invalid
        print("The provided path is not a valid directory.")  

    # Final confirmation message
    print("File organization complete.")  
   

