class Student:
    def __init__(self , ID , Student_code , name , family , role=0):
        self.ID = ID
        self.Student_code = Student_code
        self.name = name
        self.family = family
        self.role = role
    def __str__(self):
        return f"fullname = {self.name} {self.family} code = {self.Student_code}"