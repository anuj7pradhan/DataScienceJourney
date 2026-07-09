# Abstraction

    # Hiding unnecessary details from users through class and methods


"""
class Student:  # Student class
   
    def __init__(self,f_name, class_grade,percentage):     # This is method
        self.name = f_name      # This is attribute
        self.grade = class_grade    # This is attribute
        self.percentage = percentage


    def student_details(self):  # Method - Abstraction
        print(f"{self.name} is in class {self.grade} and with {self.percentage + 2}%")  # Hidden from users

# object - instance of class
student1 = Student("Sisa",11,88)    # This is object
student2 = Student("Sunil", 12,76)  # This is object

# print(student1.percentage)
student1.student_details()
"""


# Encapsulation
"""
class Student:  # Student class
   
    def __init__(self,f_name, class_grade,percentage):     # This is method
        self.name = f_name      # This is attribute
        self.grade = class_grade    # This is attribute
        self.__percentage = percentage # Double underscore limits access

    def get_percentage(self):   # New method to access the attribute
        return self.__percentage

    def student_details(self):  # Method
        print(f"{self.name} is in class {self.grade} and with {self.percentage}%")  # Hidden from users

# object - instance of class
student1 = Student("Sisa",11,88)    # This is object
student2 = Student("Sunil", 12,76)  # This is object

# print(student1.percentage)
# student1.student_details()
print(student1.get_percentage())
print(student2.get_percentage())
"""


# Inhertance
    # Allows one class (child) to reuse the prop and methods of another class (parent)

# This is parent class
"""
class Student:  # Student class
   
    def __init__(self,f_name, class_grade,percentage):     # This is method
        self.name = f_name      # This is attribute
        self.grade = class_grade    # This is attribute
        self.percentage = percentage # Double underscore limits access


    def student_details(self):  # Method
        print(f"{self.name} is in class {self.grade} and with {self.percentage}%")  # Hidden from users

# object - instance of class
student1 = Student("Sisa",11,88)    # This is object
student2 = Student("Sunil", 12,76)  # This is object


# This is child class

class GraduateStudent(Student): # GraduateStudent child class inherit prop and methods fromm Student parent class
    def __init__(self, f_name, class_grade, percentage, stream): # Parameters from parent clas and new parameter in child class
        super().__init__(f_name, class_grade, percentage)   # Call parent class intializer
        self.stream = stream    # Ths is new attribute in child class


    def student_details(self):
        super().student_details()   # Method inherit from parent class
        print(f"Stream is {self.stream}")


# Object
Grad_Student1 = GraduateStudent("Suren", 12,96,"PCM")
print(Grad_Student1.student_details())
"""


# Polymorphism
    # Allows methods in different classes to have same name 
    # but different behaviour depending on an objects.
"""
class Student:  # Student class
    def __init__(self, name, grade, percentage):
        self.name = name        # Attributes
        self.grade = grade
        self.percentage = percentage

    def student_details(self):  # Method
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# Object - instance of class
student1 = Student("Samikchya", 12, 87)
student2 = Student("Praphool", 11, 89)

# Child Class
class GraduateStudent(Student):
    def __init__(self, name, grade, percentage,stream):
        super().__init__(name, grade, percentage)
        self.stream = stream

    def student_details(self):  #This is method
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%  and from Stream {self.stream}")

# Object Student class
student1 = Student("Sasmit", 12,76)


# Object GraduateStudent class
Grad_Student1 = GraduateStudent("Suresh", 11, 67, "MCS")
student1.student_details()
Grad_Student1.student_details()
"""


 