# OOPs in Python

# Two ways of programming in Python:
    # 1. Procedural Programming
    # 2. OOPs

# OOPs: Object Oriented Programming
    # A way of organizing code by creating "blueprints"(called classes) 
    # to represent real-world things like student, car, or house. 
    # These blueprints help you create objects (indivisual examples of those things) and 
    # define their behavior.
# Class:
    # A class is a blueprint or templete for crating objects.
    # It defines the properties (attributes) & actions/ behaviors (methods) type will have.

# Object:
    # An object is a specific instance of a class.
    # It has actual data based on the blueprint defined by the class. 



# OOPs in Python
# OOP - Object Oriented Programming

# Student detatils
# student_1 = ["Apsara",10] # Name, Grade
# student_2 = ["Aisa",12]

# print(student_1)
# print(student_1[0])
# print(f"{student_1[0]} is in class {student_1[1]}")
# print(f"{student_2[0]} is in class {student_2[1]}")

"""
Why OOPs?
    1. Models Real-World Problems
        ->  Mimics real-world entires for easier understanding
    2. Code Reusability
        ->  Encourages reusable, mmodular, and organized code
    3. Easier Maintenance
        ->  OOP recognizes code into small, manageable parts (class and objects). 
            Changes in one part doesn't impact others, making it easier to maintain.
    4. Encapsulation
        ->  Encapsulation protects data integrity and privacy by building data and methods.
    5.lexibility and Scaling
        ->  OOP makes it easier to add new features without affecting existing code.
"""

# USING OOPS for creating student records

    # class - blueprint/template
# class Student:
#     # pass
#     name = "Suresh"
#     grade = 10
# # object - instance of class
# student1 = Student()
# print(f"My name is {student1.name} and I study in {student1.grade}th grade.")

# student2 = Student()
# print(f"My name is {student2.name} and I study in {student2.grade}th grade.")

"""
class Student:  # Student class
    # value initializing __init__ method - constructor - fix
    # self - reference or connection build between class and object - fix
    
    def __init__(self,f_name, class_grade):     # This is method
        self.name = f_name      # This is attribute
        self.grade = class_grade    # This is attribute

# object - instance of class
student1 = Student("Sisa",11)
print(f"My name is {student1.name} and I study in {student1.grade}th grade.")

student2 = Student("Sunil", 12)
print(student2.name, student2.grade)

student3 = Student("Balaram", 12)
print(student3.name,student3.grade)

"""




"""
# class - Blueprint or template
# value initializing __init__ method - constructor - fix
# self - reference or connection build between class and object - fix
    
class Student:  # Student class

    # value initializing __init__ method - constructor - fix
    # self - reference or connection build between class and object - fix
    
    def __init__(self,f_name, class_grade,percentage):     # This is method
        self.name = f_name      # This is attribute
        self.grade = class_grade    # This is attribute
        self.percentage = percentage

    def student_details(self):  # Method
        print(f"{self.name} is in class {self.grade}")


# # object - instance of class
student1 = Student("Sisa",11,88)
# print(f"My name is {student1.name} and I study in {student1.grade}th grade.")

student2 = Student("Sunil", 12,76)
# print(student2.name, student2.grade)

# student3 = Student("Balaram", 12,88)
# print(student3.name,student3.grade)

student1.student_details()
student2.student_details()

print(f"This is old percentage: {student1.percentage}")
student1.percentage = 90    # modify
print(f"This is updated percentage: {student1.percentage}")


# delete object property

print(student1.__dict__)
del student1.percentage
print(student1.__dict__)

# Delete object
# del student1
# print(student1)
"""

"""
class House:
    
    
    def __init__(self,address,total_room,total_kitchen,total_washroom):
        self.address = address
        self.total_room = total_room
        self.total_kitchen = total_kitchen
        self.total_washroom = total_washroom
    

    def house_details(self):
        print(f"I am from {self.address}. It contains {self.total_room} rooms,{self.total_kitchen} kitchen and {self.total_washroom} washrooms.")

house1 = House("Kirtipur",2,1,3)
house1.house_details()

house2 = House('Bhajangal',4,2,4)
house2.house_details()


"""
# class - Blueprint or template
# value initializing __init__ method - constructor - fix
# self - reference or connection build between class and object - fix
    
class Student:  # Student class
   
    def __init__(self,f_name, class_grade,percentage,team):     # This is method
        self.name = f_name      # This is attribute
        self.grade = class_grade    # This is attribute
        self.percentage = percentage
        self.team = team


    def student_details(self):  # Method
        print(f"{self.name} is in class {self.grade} and is from team {self.team}")


team1 = 'A'
team2 = 'B'
# object - instance of class
student1 = Student("Sisa",11,88,team1)
print(f"My name is {student1.name} and I study in {student1.grade}th grade. i am from team {student1.team}")

student2 = Student("Sunil", 12,76,team2)
print(student2.name, student2.grade)

student3 = Student("Balaram", 12,88,team1)
print(student3.name,student3.grade)

print(f"I am from {student1.team} team")
print(f"I am from {student2.team} team")
print()
student1.student_details()
student2.student_details()


"""Question

Create a Python program using Single Inheritance to manage a student's academic record.

Requirements
Create a parent class named Person.
Data members:
name
age
Create a constructor to initialize these values.
Create a method display_person() to display the person's details.
Create a child class named Student that inherits from Person.
Additional data members:
roll_no
faculty
Marks in:
Python
Java
DBMS
Networking
AI
Initialize all required data members.
Create the following methods:
calculate_total()
calculate_percentage()
calculate_grade()

Display:
Student Name
Age
Roll Number
Faculty
Marks of all subjects
Total Marks
Percentage
Grade
Create one object of the Student class and display the complete result.
"""