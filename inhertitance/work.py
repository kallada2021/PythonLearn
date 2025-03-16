class Person:
    def __init__(self, name):
        self.name = name
    
    def person_info(self):
        print(f"My name is {self.name}")

class Employee(Person):
    def __init__(self, name, jobtitle):
        Person.__init__(self,name)
        self.jobtitle = jobtitle
    
    def work(self):
        print(f"{self.name} is a {self.jobtitle}")

class Manager(Employee):
    def __init__(self, name, jobtitle):
        Employee.__init__(self, name, jobtitle)
    
    def manage(self,name,jobtitle):
        # print(f"{self.name} manages {employee.name} who is a {employee.jobtitle}")
        print(f"{self.name} manages {name} who is a {jobtitle}")



person = Person("Robert")
person.person_info()
employee = Employee("robert", "welder")
employee.work()
manager = Manager("Thomas","ProjectManager")
manager.manage(employee.name, employee.jobtitle)
# manager.manage()

# Thomas manages Robert who is a welder