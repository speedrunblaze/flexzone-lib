
# FlexZone - A Flexible File Management Library

FlexZone is a lightweight Python library designed to automate file management tasks. It allows users to create, read, delete, move, and copy files easily.

## Features:
- Create, read, delete, move, and copy files.
- List files in the specified directory.
- Ensure that directories are created if they don't exist.

## Installation:
Install the library using `pip`:

```bash
pip install git+https://github.com/speedrunblaze/flexzone-lib.git
```

## Usage Example:

```python
from flexzone.file_manager import FileManager

manager = FileManager("your_directory")
manager.create_file("example.txt", "This is a sample file.")
content = manager.read_file("example.txt")
print(content)
```
