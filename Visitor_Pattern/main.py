from visitable import File, Directory
from visitor import FileListVisitor, SizeCalculatorSize, ExtensionCounterVisitor


dir1 = Directory(name='Directory1')
dir2 = Directory(name='Direcotry2', parent=dir1)
dir3 = Directory(name='Direcotry3', parent=dir1)
file1 = File(name='File1', size=15, extension='.txt', parent=dir1)
file2 = File(name='File2', size=15, extension='.jpg', parent=dir2)
file3 = File(name='File3', size=30, extension='.txt', parent=dir3)
file4 = File(name='File4', size=15, extension='.png', parent=dir3)

FileListVisitor = FileListVisitor()
dir1.accept(FileListVisitor)
for element in FileListVisitor.elements:
    print(element)
print('-' * 30)

SizeCalculatorSize = SizeCalculatorSize()
dir1.accept(SizeCalculatorSize)
print(SizeCalculatorSize.total_size)
print('-' * 30)

ExtensionCounterVisitor = ExtensionCounterVisitor()
dir1.accept(ExtensionCounterVisitor)
print(ExtensionCounterVisitor.extensions)
