class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

student1 = Student("Yash")
student2 = Student("Rahul")

Student.college = "XYZ College"

print(student1.college)
print(student2.college)
