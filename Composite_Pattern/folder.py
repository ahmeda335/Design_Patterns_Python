from IFileSystem import FileSystemItem

class Folder(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self.items = []

    def add(self, item):
        self.items.append(item)

    def display(self, indent=0):
        print(' ' * indent + f'+ Folder: {self.name}')
        for item in self.items:
            item.display(indent + 2)

    def get_size(self):
        return sum(item.get_size() for item in self.items)