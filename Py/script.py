import os
import shutil
from colorama import init, Fore

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def organize_files(source_dir, target_dir):
    file_extensions = {
        "Documentos": [".txt", ".doc", ".docx", ".pdf"],
        "Fotos": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Música": [".mp3", ".wav", ".flac"],
        "Descargas": [".zip", ".rar", ".exe"],
    }

    other_folder = os.path.join(target_dir, "Otros")
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
                        print(f"{Fore.GREEN}Moved {file_name} to {target_folder}")
                        moved = True
                        break
                    except shutil.Error as e:
                        print(f"{Fore.RED}Error moving {file_name}: {e}")
            if not moved:
                target_path = os.path.join(other_folder, file_name)
                try:
                    shutil.move(file_path, target_path)
                    print(f"{Fore.YELLOW}Moved {file_name} to {other_folder}")
                except shutil.Error as e:
                    print(f"{Fore.RED}Error moving {file_name}: {e}")

if __name__ == "__main__":
    init()  # Inicializar colorama

    target_dir = r"C:\Users\casti\Videos\Organizados"
    create_folder_if_not_exists(target_dir)

    source_dir = r"C:\Users\casti\Videos"

    organize_files(source_dir, target_dir)