class A:
    def __init__(self):
        print("Initilaizing A.")
    
    def method(self):
        print("Method in A.")


class B(A):
    def __init__(self):
        super().__init__()
        print("Initiailizing B.")
    
    def method(self):
        super().method()
        print("Method in B.")


class C(B,A):
    def __init__(self):
        super().__init__()
        print("Initializing C.")

    def method(self):
        super().method()
        print("Method in C.")

class D(C,B,A):
    def __init__(self):
        super().__init__()
        print("Initializing D.")
    
    def method(self):
        super().method()
        print("Method in D.")

d = D()
d.method()
