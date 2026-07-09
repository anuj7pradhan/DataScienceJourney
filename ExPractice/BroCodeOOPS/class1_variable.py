# class variables -> Shared among all instances of a class
#                 -> Defined outside the constructor
#                 -> Allow you to share data among all objects created fromm that class


class Student:
    class_year = 2026       # This is a class variable
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Sumnima",22)
student4 = Student("Pramila",22)

print(student1.name)
print(student1.age)
print(Student.class_year)

print()

print(student2.name)
print(student2.age)
print(Student.class_year)   # Access variable directly from the class

print(Student.num_student)

print(f"My graduating class of {Student.class_year} has {Student.num_student} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
# https://youtu.be/IbMDCwVm63M
