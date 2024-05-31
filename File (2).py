import os
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def copy_files(source_folder, backup_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            backup_path = os.path.join(backup_folder, root.replace(source_folder, ""), file)

            try:
                os.makedirs(os.path.dirname(backup_path), exist_ok=True)
                shutil.copy2(source_path, backup_path)
                logging.info(f'Copied {source_path} to {backup_path}')
            except Exception as e:
                logging.error(f'Error copying {source_path} to {backup_path}: {e}')

def delete_extraneous_files(source_folder, backup_folder):
    for root, _, files in os.walk(backup_folder):
        for file in files:
            backup_path = os.path.join(root, file)
            source_path = os.path.join(source_folder, root.replace(backup_folder, ""), file)

            if not os.path.exists(source_path):
                try:
                    os.remove(backup_path)
                    logging.info(f'Removed {backup_path}')
                except Exception as e:
                    logging.error(f'Error removing {backup_path}: {e}')

def backup_and_sync(source_folder, backup_folder):
    copy_files(source_folder, backup_folder)
    delete_extraneous_files(source_folder, backup_folder)

if __name__ == '__main__':
    source_folder = r"D:\ANITS\Python\File_sync\Folder 1"
    backup_folder = r"D:\ANITS\Python\File_sync\Folder 2"
    backup_and_sync(source_folder, backup_folder)
