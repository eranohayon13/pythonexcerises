class Students:
    def __init__(self, age, class_, name = "student"):
        self.age = age
        self.class_ = class_
        self.name = name

    def average(self, average1, average2, average3):
        return (average1+average2+average3)/3

student = Students(27,3,"Bilbo")
print(student.average(76, 65, 13))
print(getattr(student,"age"))