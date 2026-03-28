import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")

    print("All .jpg files moved successfully!")

source_folder = "source_folder_path"
destination_folder = "destination_folder_path"

move_jpg_files(source_folder, destination_folder)