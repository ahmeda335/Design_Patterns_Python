from file import File
from folder import Folder

if __name__ == '__main__':
    # Create files
    file1 = File('photo.jpg', 1500)
    file2 = File('report.docx', 300)
    file3 = File('music.mp3', 5000)

    # Create folders
    docs = Folder('Documents')
    media = Folder('Media')
    root = Folder('Root')

    # Compose structure
    docs.add(file2)
    media.add(file1)
    media.add(file3)

    root.add(docs)
    root.add(media)

    # Display
    root.display()
    print(f"Total Size: {root.get_size()}KB")