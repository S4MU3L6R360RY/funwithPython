import shutil
import os

def copy_music_files(source_file, destination_dir):
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Read the list of file locations
    with open(source_file, 'r', encoding='utf-8') as file:
        file_locations = file.readlines()

    # Copy each file to the destination directory
    for file_location in file_locations:
        file_location = file_location.strip()  # Remove any leading/trailing whitespace
        if os.path.exists(file_location):
            try:
                shutil.copy(file_location, destination_dir)
                print(f"Copied: {file_location}")
            except Exception as e:
                print(f"Error copying {file_location}: {e}")
        else:
            print(f"File not found: {file_location}")

if __name__ == "__main__":
    source_file = 'music_files.txt'        # Text file containing the list of music file locations
    destination_dir = '/home/samgregory/Music/playlistforwork'      # Destination directory on the SD card

    copy_music_files(source_file, destination_dir)
    print("Music files copied successfully.")
