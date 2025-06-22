from caretaker import CareTaker
from text_editor import TextEditor

TEXT_EDITOR = TextEditor()
CARETAKER = CareTaker(TEXT_EDITOR)

TEXT_EDITOR.write("I love python")
CARETAKER.save()

TEXT_EDITOR.write("I love C++")
CARETAKER.save()

TEXT_EDITOR.write("I love Go") # I didn't save this.

# Making Undo
CARETAKER.restore(-1)
print(TEXT_EDITOR)

# Making another Undo
CARETAKER.restore(-2)
print(TEXT_EDITOR)
