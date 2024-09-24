class Employee:
    def __init__(self, f, l, s):
        self.firstName = f
        self.lastName = l 
        self.salary = s
    def GiveRaise(self, r):
        self.salary += r