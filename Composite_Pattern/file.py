from IFileSystem import FileSystemItem

class File(FileSystemItem):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def display(self, indent=0):
        print(' ' * indent + f'- File: {self.name} ({self.size}KB)')

    def get_size(self):
        return self.size