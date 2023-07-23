import os
import shutil
from colorama import init, Fore

# 📂 Function to create a folder if it doesn't exist
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 📁 Organize files into target folders based on their extensions
def organize_files(source_dir, target_dir):
    file_extensions = {
        "Documents": [".txt", ".doc", ".docx", ".pdf"],
        "Photos": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Music": [".mp3", ".wav", ".flac"],
        "Downloads": [".zip", ".rar", ".exe"],
    }

    other_folder = os.path.join(target_dir, "Others")
    create_folder_if_not_exists(other_folder)

    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()
            moved = False
            for folder, extensions in file_extensions.items():
                if file_extension in extensions:
                    target_folder = os.path.join(target_dir, folder)
                    create_folder_if_not_exists(target_folder)
                    target_path = os.path.join(target_folder, file_name)
                    try:
                        shutil.move(file_path, target_path)
                        print(f"{Fore.GREEN}Moved {file_name} to {target_folder} 🚚")
                        moved = True
                        break
                    except shutil.Error as e:
                        print(f"{Fore.RED}Error moving {file_name}: {e} ❌")
            if not moved:
                target_path = os.path.join(other_folder, file_name)
                try:
                    shutil.move(file_path, target_path)
                    print(f"{Fore.YELLOW}Moved {file_name} to {other_folder} 🚚")
                except shutil.Error as e:
                    print(f"{Fore.RED}Error moving {file_name}: {e} ❌")

if __name__ == "__main__":
    init()  # 🎨 Initialize colorama

    # 🎯 Set the target directory to organize files into
    target_dir = r"C:\Users\casti\3D Objects\Organized"  # You can add your own folder and modify it to your liking
    create_folder_if_not_exists(target_dir)

    # 📂 Set the source directory containing the files to be organized
    source_dir = r"C:\Users\casti\3D Objects"

    # 🚀 Start organizing files
    organize_files(source_dir, target_dir)