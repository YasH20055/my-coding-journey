class Student:

    college = "ABC College"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()
