class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I'm a pet")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("MEOW")

    def purr(self):
        print("Purrr")

    def show(self):
        print(f"I am {self.name} and I am {self.age} and I am {self.color}")

myCat = Cat("Fluffy", 3, "Calico")
myCat.show()
myCat.speak()

class Dog(Pet):
    def speak(self):
        print("WOOF")


p = Pet("Buddy", 8)
p.show()

class Person:
    num_people = 0

    def __init__(self, name) -> None:
        self.name = name
        Person.add_person()

    @staticmethod
    def num_meals(meals):
        if meals == 3:
            print(f"Three meals a day")
        else:
            print(f"Not three meals a day")

    @classmethod
    def number_people(cls):
        return cls.num_people

    @classmethod
    def add_person(cls):
        cls.num_people += 1
print(Person.num_people)
p1 = Person("Bob")
p2 = Person("Omar")
p2.num_meals(3)
print(Person.num_meals(5))
# print(p2.num_people)
print(Person.num_people)
# print(Person.number_people())
# print(Person.num_meals(3))

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        print(self.students)
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Abdullah", 19, 98)
s2 = Student("Tim", 22, 90)
s3 = Student("Fatimah", 19, 79)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)


# print(course.students[1].name)
# print(course.get_average_grade())
# print(course.add_student(s1))