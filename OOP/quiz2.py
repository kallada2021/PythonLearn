class Parent:
    def __init__(self):
        self.value = "Parent"
    
    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Child"


parent = Parent()
parent.show()

child = Child()
child.show()