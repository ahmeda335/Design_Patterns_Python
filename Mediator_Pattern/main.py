from mediator import Mediator
from student import Student


MEDIATOR = Mediator()

student1 = Student("Ahmed")
student2 = Student("Mohamed")
student3 = Student("Ali")

MEDIATOR.add_student(student1)
MEDIATOR.add_student(student2)
MEDIATOR.add_student(student3)

MEDIATOR.show_students()
print('-' * 30)

MEDIATOR.send_message(student1, "Hello, I am Ahmed")
print('-' * 30)
MEDIATOR.send_message(student2, "Mohamed is here!")