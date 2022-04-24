class Lesson:
    def __init__(self , ID , Lesson_code , name , book , Time):
        self.ID = ID
        self.Lesson_code = Lesson_code
        self.name = name
        self.book = book
        self.Time = Time

    def __str__(self):
        return f"{self.name} code = {self.Lesson_code} Time = {self.Time}"
