
from flexzone.file_manager import FileManager

manager = FileManager("test_dir")
manager.create_file("example.txt", "Content for the example file.")
print(manager.read_file("example.txt"))
    