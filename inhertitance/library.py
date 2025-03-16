'''
You are developing a library management system. In this system, you have the following classes and relationships:

Person: This is the base class that includes common attributes like name and email.

Member: This class should inherit from Person and includes additional attributes like membership_id and borrowed_books.

Librarian: This class should inherit from Person and includes additional attributes like employee_id and work_shift.

SeniorLibrarian: This class should inherit from Librarian and adds attributes like years_of_experience and managed_sections.

Based on the scenario above, determine which types of inheritance are used. Explain your reasoning and how each inheritance type applies to the relationships between the classes.
'''

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        print(f"My name is {self.name} and my email id is {self.email}")

class Member(Person):
    def __init__(self, name, email, membership_id, borrowed_book):
        self.membership_id = membership_id
        self.borrowed_book = borrowed_book
        super().__init__(name, email)
        print(borrowed_book)

class Librarian(Person):
    def __init__(self, name, email, employee_id, work_shift):
        self.employee_id = employee_id
        self.work_shift =  work_shift
        super().__init__(name, email)
        print(f"{self.name}'s employee id is {self.employee_id} and works {self.work_shift} shift")

class SeniorLibrarian(Librarian):
    def __init__(self, name, email, employee_id, work_shift, years_of_experience, managed_shifts, empname):
        self.years_of_experience = years_of_experience
        self.managed_shifts = managed_shifts
        super().__init__(name, email, employee_id, work_shift)
        print(f"{self.name} manages {self.managed_shifts} shifts and has {self.years_of_experience} and works the {self.work_shift} and manages {empname}")



member = Member("Tom", "tom123@yahoo.com", "A34560", "Adventures of Tom Sawyer")
librarian = Librarian("Fred","fred4567@gmail.com","E8901","evening")
seniorlibrarian = SeniorLibrarian("Micheal", "michael345@lib.org", "M34", "morning", 10, "all", librarian.name)