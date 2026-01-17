import os
import shutil
import sys

FILE_TYPES = {
    "Images": ["jpg", "jpeg", "png"],
    "Documents": ["pdf", "txt", "docx"],
    "Videos": ["mp4", "mkv"],
    "Archives": ["zip", "rar"]
}

def get_folder(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder
    return "Others"

def organize_files(directory):
    if not os.path.exists(directory):
        print("Invalid directory path.")
        return

    files = os.listdir(directory)

    if not files:
        print("Directory is empty.")
        return

    for file in files:
        source_path = os.path.join(directory, file)

        if os.path.isfile(source_path):
            extension = file.split(".")[-1].lower() if "." in file else ""
            folder_name = get_folder(extension)

            target_dir = os.path.join(directory, folder_name)
            os.makedirs(target_dir, exist_ok=True)

            target_path = os.path.join(target_dir, file)

            try:
                shutil.move(source_path, target_path)
                print(f"Moved: {file} -> {folder_name}")
            except Exception:
                print(f"Failed to move: {file}")

    print("File organization completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a directory path.")
    else:
        organize_files(sys.argv[1])
