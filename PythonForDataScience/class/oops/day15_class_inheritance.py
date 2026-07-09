# # Inheritance
# # Syntax
# class ParentClass:      # Base class pani bhanincha
#     # Parent class attributes and methods
#     pass

# class ChildClass (ParentClass):     # Derived class pani bhanincha
#     # Child class attributes and methods
#     pass

# # Code reusability
# # Easy maintinance
# # Reduce duplicate code
# # Extensibility


# # Parent class -> Base class
# # Child class -> Derived class


# # Types of Inheritance
# # 1. single Inheritance
# # 2. Multiple Inheritance
# # 3. Multilevel Inheritance
# # 4. Hierarchical Inheritance


# # 1. single Inheritance:
#     # !. 1 parent and 1 child

# class Animal:   # Making parent class
#     def sound(self):    # Attributes of parent class
#         print("Animal makes sound.")

# class Dog(Animal):  # Making child class and inheritate the parent class
#     def bark(self):     # Attributes of child class
#         print("Dog barks")

# animal1 = Dog() # Object of child
# animal1.sound()
# animal1.bark()

# animal2 = Animal()
# animal1.sound()
# animal1.bark()


# 2. Multiple Inheritance


"""class Father:
    def skill1(self):
        print("Teaching")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Playing")

ob1 = Child()
ob1.skill1()
ob1.skill2()
ob1.skill3()
"""

"""
Create a Python program using Multiple Inheritance.
Requirements:
Create a class Calculator with a method add(a, b).
Create another class Multiplier with a method multiply(a, b).
Create a class MathOperations that inherits from both classes.
Create an object and display the sum and multiplication of 10 and 5.

"""


class Calculator:
    def add(self,a,b):
        return a + b
    
class Multiplier:
    def multiply(self,a,b):
        return a * b
    
class MathOperations(Calculator, Multiplier):
    pass

obj1 = MathOperations()
print(f"Sum: {obj1.add(12,13)}")
print(f"Multiply: {obj1.multiply(12,1)}")


class GrandParent:
    def show1(self):
        print("This is me GrandParent.")

class Parent(GrandParent):
    def show2(self):
        print("This is Parent.")

class Child(Parent):
    def show3(self):
        print("This is child.")

child1 = Child()
child1.show1()
child1.show2()




# Create a Python program using Multilevel Inheritance.

# Requirements:

# Create a class Person with a method walk().
# Create a class Student that inherits from Person and has a method study().
# Create a class CollegeStudent that inherits from Student and has a method attend_class().
# Create an object of CollegeStudent.
# Call all methods.




class Person:
    def walk(self):
        print("Walk")

class Student(Person):
    def study(self):
        print("Student")

class CollegeStudent(Student):
    def attend_class(self):
        print("CollegeStudent")

col1 = CollegeStudent()
col1.walk()
col1.study()
col1.attend_class()


# 4. Hierarchical Inheritance


class Vehicle:
    def info(self):
        print("Vehicle moves")

class car(Vehicle):
    def info_car(self):
        print("Car info")

class bike(Vehicle):
    def info_bike(self):
        print("bike info")

v1 = car()
v1.info()
v1.info_car()

"""
Create a Python program using Hierarchical Inheritance.

Requirements:

Create a parent class Animal with a method eat().
Create two child classes:
Dog with a method bark()
Cat with a method meow()
Create objects of both child classes.
Call the inherited method and their own methods.
"""


class Animal:
    def eat(self):
        print("Eat")

class dog(Animal):
    def bark(self):
        print("Bark")

class cat(Animal):
    def meow(self):
        print("Meow")

animal1 = dog()
animal1.bark()
animal1.eat()

animal2 = cat()
animal2.meow()
animal2.eat()