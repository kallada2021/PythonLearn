class Person:
    def __init__(self, name):
        self.name = name
    
    def person_info(self):
        print(f"My name is {self.name}")
    
    def change_name(self,name):
        self.name = name
        print(f"My name is {self.name}")

class Student(Person):
    def __init__(self, name):
        self.name = name
        
    def study(self):
        print(f"{self.name} is studying History")

class Teacher(Student):
    def __init__(self, name):
        super().__init__(name)
    def teach(self, name):
        print(f"{self.name} is teaching {name}")


person = Person("Bob")
print(f"My name is {person.name}")
person.person_info()
person.change_name("Mick")
student = Student("Tom")
student.study()
teacher = Teacher("Rachel")
teacher.teach("Tom")