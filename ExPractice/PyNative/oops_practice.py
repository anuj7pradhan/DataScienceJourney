# Exercise 1: Define an Empty Vehicle Class

"""
class Vehicle():
    pass
print(Vehicle)
"""

"""
# Exercise 2: Vehicle Class with Instance Attributes
# Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. 
    # Create an object of the class and print both attributes.
class Vehicle():
    def __init__(self,vehicle_name,max_speed, mileage):
        self.vehicle_name = vehicle_name    # assign each parameter to self to store them as instance attributes.
        self.max_speed = max_speed  # assign each parameter to self to store them as instance attributes.
        self.mileage = mileage  # assign each parameter to self to store them as instance attributes.

vehicle1 = Vehicle("Tesla Model S",250,18)
print(f"{vehicle1.vehicle_name} has max speed of {vehicle1.max_speed} and it's milage is {vehicle1.mileage}")

"""


# Exercise 3: Rectangle Class with Area & Perimeter
# Write a Python program to create a Rectangle class 
# with length and width as instance attributes, 
# and two methods: area() that returns the area 
# and perimeter() that returns the perimeter.

"""
class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
rectangle1 = Rectangle(10,4)
print(f"Area: {rectangle1.area()}")
print(f"Perimeter: {rectangle1.perimeter()}")
"""

"""
# Exercise 4: Student Class with Average Grade
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
    
student1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"{student1.name}'s Average grade is", student1.average())
"""

# Exercise 5: Product Class with Stock Value Calculator

"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def total_value(self):
        return self.price * self.quantity


product1 = Product("Noodles", 25, 5)
print(f"Your {product1.name} costs {product1.total_value():.3f}")

product2 = Product("Mac", 250000.326, 3)
print(f"Your {product2.name} costs {product2.total_value():.2f}")
"""
# Exercise 6: Bank Account with Deposit & Overdraw Protection
# Write a Python program to create a BankAccount class with a balance attribute 
# and two methods: deposit(amount) that adds funds to the balance, 
# and withdraw(amount) that deducts funds but prevents the balance from going below zero.
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    

    def deposit(self,amount):
        self.balance +=  amount
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance after withddraw: {self.balance}")
        else:
            print(f"Insufficient funds, Current balance is: {self.balance}")
customer1 = BankAccount(1000)
customer1.deposit(500)
customer1.withdraw(200)
customer1.withdraw(2000)
"""

# Exercise 7: Light Class with On/Off State Toggle
# WAP to create a Light class with three methods: 
#   turn_on() that switches the light on, 
#   turn_off() that switches it off, 
#   and status() that reports whether the light is currently on or off.

# class Light:
#     def __init__(self):
#         self.is_on = False

#     def turn_on(self):
#         self.is_on = True
#         print("Light is ON.")

#     def turn_off(self):
#         self.is_on = False
#         print("Light is OFF")

#     def status(self):
#         state = "ON" if self.is_on else "OFF"
#         print(f"Current status: {state}")

# light1 = Light()
# light1.turn_on()
# light1.status()
# light1.turn_off()
# light1.status()


"""
class Light:
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print("Light is ON")
    
    def turn_off(self):
        self.is_on = False
        print("Light is OFF")
    
    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current status: {state}")

light1 = Light()
light1.turn_on()
light1.status()
light1.turn_off()
light1.status()
"""

# Exercise 8: User Class with Password Validation
# WAP to create a User class that stores 
# a username and a password. 
# Add a check_password(input_password) method 
# that returns True if the input matches the stored password, 
# and False otherwise.
"""
class User:
    def __init__(self,username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password
        
user1 = User("anuj","anuj123")
print(user1.check_password(input("Enter password: ")))

print(f"This is a wrong password: {user1.check_password("wrongpassword")}")
"""


# Exercise 9: Temperature Class with Unit Converters
# WAP to create a Temperature class that stores a temperature in Celsius. 
# Add two methods: to_fahrenheit() that converts 
# and returns the value in Fahrenheit, 
# and to_kelvin() that converts 
# and returns the value in Kelvin.

"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def kelvin(self):
        return self.celsius + 273.15
    
temp = Temperature(100)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit():.2f}")
print(f"Kelvin: {temp.kelvin():.2f}")
"""


# Exercise 10: Notebook Class with Add & Display Notes
# WAP to create a Notebook class that maintains an internal list of notes. 
# Add an add_note(note) method that appends a new note to the list, 
# and a show_notes() method that prints all stored notes.
"""
class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self,note):
       self.notes.append(note)
    
    def show_notes(self):
        for i, note in enumerate(self.notes, start= 1):
            print(f"{i}.{note}")

nb = Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_notes()
"""