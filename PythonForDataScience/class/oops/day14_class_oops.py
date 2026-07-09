# # OOPS
# # Programming paradigms
# # 1. Procedural programming language
# # 2. OOP


# # OOPS: 
#     # Organized
#     # Easy to maintain
#     # Reusability
        
# # Class: Blueprint of object, it can define behavior and attributes of objects.
# # Object: Multiple objects can be created from the same class.
# # Constructor: It is automatically called whenever an object is created

#     # Purpose:
#         # Initialize object attributes
#         # Assign initial values to an object

# # The 'self' keyword
#     # 'self' refrers to the current object
#     # it is used to access the attributes and methods of that objects

# # Class:
# class Student:
#     def __init__(self,name,age):
#         self.name = name    # Attributes
#         self.age = age

#     def show(self):  #methods
#         print(f"This is me {self.name} and i am {self.age}.")

# ob = Student("Ram",33)
# ob.show()

# ob1 = Student("Hari",12)
# ob1.show()



# # Object:



# class Area:
#     def __init__(self,length,height):
#         self.length = length
#         self.height = height
#     def show(self):
#         print(f"Area is {self.length * self.height}")

# area1 = Area(2,3)
# area1.show()


# area2 = Area(3,4)
# area2.show()

# class Shop:

#     def __init__(self, Pname, price, quantity):
#         self.Pname = Pname
#         self.price = price
#         self.quantity = quantity


#     def show(self):
#         print(f"Total price of {self.Pname} is {self.price * self.quantity}")

# samaan = Shop("Nimki",200,4) 
# samaan.show()


# #area
# #perimeter


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    

#     def area(self):
#         print(f"Area is {3.14 * self.radius * self.radius}")

#     def perimeter(self):
#         print(f"Perimeter is {2 * 3.14 * self.radius}")

# circle1 = Circle(2)
# circle1.area()
# circle1.perimeter()

# # Task - 2

# Question: Student Grade System (OOP)

# Create a class named Student with the following attributes:

# name
# marks

# Create a method named grade() that displays the student's grade based on the following criteria:

# Marks	Grade
# 90 and above	A
# 80 – 89	B
# 70 – 79	C
# 60 – 69	D
# Below 60	Fail

# Instructions:

# Create a constructor (_init_()) to initialize the student's name and marks.
# Take the student's name and marks as input from the user.
# Create a Student object.
# Call the grade() method to display the student's grade.


class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if marks >= 90:
            print("Grade A")
        elif marks >= 80 and marks <= 89:
            print("Grade B")
        elif marks >= 70 and marks <= 79:
            print("Grade C")
        elif marks >= 60 and marks <= 69:
            print("Grade D")
        elif marks <= 60:
            print("Fail")
        else:
            print("Invalid marks")


name = input("Enter your name: ")
marks = int(input("Enter marks: "))

st1 = Student(name, marks)
print(f"\nStudent name: {st1.name}")
print(f"Marks is {st1.marks}")
st1.grade()



