print("Task 1 - Instance and class attributes")

class Student:

    university = "NSU"
    def __init__(self, name):
        self.name = name
# Создат Анна и Омар
anna = Student("Anna")
omar = Student("Omar")


print(anna.name, anna.university)
print(omar.name, omar.university)

Student.university = "NSU Updated"

print(Student.university)


print("Task - 2 Instance and class attributes")
class Device:
    category = "General"

    
    def __init__(self, name):
       self.name = name
a = Device("Laptop")
b = Device("Printer")
a.category = "personal"
Device.category = "shared"

print(a.category)
print(b.category)
print(Device.category)

print()

print("Task 3 - Fix shared mutable state")
#Исправление общего изменяемого состояния
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_members(self, name):
        self.members.append(name)

Alpha = Team("Alpha") 
Beta = Team("Beta")

Alpha.add_members("Anna")

print(Alpha.members)
print(Beta.members)
print(Alpha.members is Beta.members)
print()

print("Task 4 - Encapsulation and validation")
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, name):
        self.members.append(name)

Alpha = Team("Alpha")
Beta = Team("Beta")
Alpha.add_member("Anna")

print(Alpha.members)
print(Beta.members)
print(Alpha.members is Beta.members)

print()

print("Task 5 - Return a copy of internal data")


class ScoreBook:
    def __init__(self):
        self._scores = []

    def add_score(self, score):
        if score <= 0 or score > 100:
            raise ValueError("Scores should be between 0 to 100")
        self._scores.append(score)

    def get_score(self):
        return self._scores.copy()
    
book = ScoreBook()
book.add_score(80)
snapshot = book.get_score() # problem detect
snapshot.append(100)
print(snapshot)

book2 = ScoreBook()
print(book2.get_score())


print()


print("Task 6 - Interit a method")

class Person:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Person: {self.name}"
    
class Visitor(Person):    
    pass
visitor = Visitor("Omar")
print(visitor.describe())
print(isinstance(visitor,Visitor))
print(isinstance(visitor, Person))
print(issubclass(Visitor, Person))

print()

print("Task 7 - Initialize a subclass with super")
class StudentPerson(Person):
    def __init__(self, name, program):
        super().__init__(name)
        self.program = program

student = StudentPerson("Anna", "AI")        
print(student.name)
print(student.program)
print(student.describe())

print()

print("Task 8 - Override a method")
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

def describe(self):
    return f"Teacher: {self.name}, subject: {self.subject}"

teacher = Teacher("Mira", "Python")
print(teacher.describe())

person = Person("Omar")
print(person.describe())


print()

print("Task 9 - Extend an inherited method")
class DetailedStudent(StudentPerson):
    def describe(self):
        return super().describe()+", program:" + self.program

    print()

print("Task 10 - Polymorphic descriptions") 

people = [
    Person("Omar"),
    Teacher("Mira", "Python"),
    DetailedStudent("Anna", "AI")

]
for person in people:
    print(person.describe())
    print()

print("Task 11 - Duck typing with shapes")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Square:
    def __init__(self,side):
        return self.side * self.side

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total
print()

print("Task 12 - Composition: a course roster")

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []
    def enroll(self,person):
        self.students.append(person)

    def roster(self):
        return [person.describe() for person in self.students]

course1 = Course("Python Basics")
course1.enroll(Teacher("Mira", "Python")) # problem detected
course1.enroll(DetailedStudent("Anna", "AI"))
for entry in course1.roster():
    print(entry)
course2 = Course("Empty course")
print(course2.roster())

print()



                          

