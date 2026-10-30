class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

student1 = Student("Yash")
student2 = Student("Rahul")

student1.name = "Amit"

print(student1.name)
print(student2.name)
