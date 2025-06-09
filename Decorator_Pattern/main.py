from text import Text
from ItalicDecorator import ItalicDecorator
from BoldDecorator import BoldDecorator
from ColorDecorator import ColorDecorator


text = "My Name is Ahmed"
print(ItalicDecorator(Text(text)))
print(BoldDecorator(ItalicDecorator(Text(text))))
print(BoldDecorator(ItalicDecorator(ColorDecorator(Text(text)))))