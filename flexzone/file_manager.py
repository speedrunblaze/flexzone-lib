
import os
import shutil
from .helpers import create_directory_if_not_exists

class FileManager:
    def __init__(self, base_path="."):
        """
        Initialize the FileManager with the given base directory.
        :param base_path: The root directory to manage files. Default is the current directory.
        """
        self.base_path = base_path
    
    def create_file(self, filename, content=""):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"File '{filename}' created.")
        else:
            print(f"The file '{filename}' already exists.")
    
    def read_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
        return None
    
    def delete_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{filename}' deleted.")
    
    def move_file(self, filename, target_directory):
        create_directory_if_not_exists(target_directory)
        file_path = os.path.join(self.base_path, filename)
        if os.path.exists(file_path):
            shutil.move(file_path, os.path.join(target_directory, filename))
            print(f"File '{filename}' moved.")
    
    def copy_file(self, filename, target_directory):
        create_directory_if_not_exists(target_directory)
        file_path = os.path.join(self.base_path, filename)
        if os.path.exists(file_path):
            shutil.copy(file_path, os.path.join(target_directory, filename))
            print(f"File '{filename}' copied.")
    
    def list_files(self):
        return os.listdir(self.base_path)
    