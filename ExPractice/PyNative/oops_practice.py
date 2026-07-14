# Exercise 1: Define an Empty Vehicle Class

"""
# Let's practice Inheritance and Class Creation in Python by defining an empty class named Vehicle.
class Vehicle():
    def __init__(self,color,speed,milage):
        self.color = color
        self.speed = speed
        self.milage = milage

    def __str__(self):
        return f"Vehicle(color = {self.color}, speed = {self.speed}, milage = {self.milage})"

class Car(Vehicle):
    def __init__(self,color,speed,milage,brand):
        super().__init__(color,speed,milage)
        self.brand = brand

    def __str__(self):
        return f"Car(\ncolor = {self.color}, \nspeed = {self.speed}, \nmilage = {self.milage}, \nbrand = {self.brand})"

car = Car("Red", 200, 15, "Toyota")
print(car)

"""

# Exercise 2: Vehicle Class with Instance Attributes
# Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. 
    # Create an object of the class and print both attributes.
"""
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

# Exercise 4: Student Class with Average Grade
"""

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

"""
class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON.")

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
# Exercise 11: Coffee Machine with Multi-Resource Tracking
# Problem Statement: Write a Python program to create a CoffeeMachine class 
# that tracks three resource attributes: water, coffee, and milk (in ml/g). 
# Add a make_latte() method that checks whether sufficient resources are available, 
# deducts them if so, and prints an appropriate message in either case.

"""class CoffeeMachine:
    def __init__(self,water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    

    def make_latte(self):
        water_required = 300
        coffee_required = 30
        milk_required = 200

        if self.water >= water_required and self.coffee >= coffee_required and self.milk >= milk_required:
            self.water -= water_required
            self.coffee -= coffee_required
            self.milk -= milk_required
            print("Latte made. successfully.")
            print(f"Remaining water: {self.water}")
            print(f"Remaining coffee: {self.coffee}")
            print(f"Remaining milk: {self.milk}")
        else:
            print(f"Not enough resources for making Latte")


machine = CoffeeMachine(400,50,300)
machine.make_latte()
"""

# Exercise 12: Shared Class Attribute Across Instances
# Problem Statement: Write a Python program to create a Vehicle class 
# with a class attribute color = "White" that is shared by all instances. 
# Create two vehicle objects and demonstrate that both share the same default color, 
# then show that changing the class attribute updates all instances that have not overridden it.


"""
class Vehicle:
    color = "White"     # Class Attribute

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

vehicle1 = Vehicle("Toyota", 230)
vehicle2 = Vehicle("BYD",300)

print()
print(f"{vehicle1.name} is in {vehicle1.color} color and it's speed is {vehicle1.speed}km/hrs")
print(f"{vehicle2.name} is in {vehicle2.color} color and it's speed is {vehicle2.speed}km/hrs")

print()
Vehicle.color = "Blue"

print(f"{vehicle1.name} is in {vehicle1.color} color and it's speed is {vehicle1.speed}km/hrs")
print(f"{vehicle2.name} is in {vehicle2.color} color and it's speed is {vehicle2.speed}km/hrs")
"""

# Exercise 13: Bus Subclass Inheriting from Vehicle
# Problem Statement: Write a Python program to create a Vehicle parent class 
# with name and max_speed attributes and a display() method. 
# Then create a Bus child class 
# that inherits everything from Vehicle without adding anything new, 
# and confirm that an instance of Bus can access the parent’s method.
"""

class Vehicle:
    def __init__(self,name,max_speed):
        self.name = name 
        self.max_speed = max_speed


    def display(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Max Speed: {self.max_speed}km/hrs")
    
class Bus(Vehicle):
    pass

bus1 = Bus("Sajha Bus", 70)
bus1.display()
"""

# Exercise 14: verride Parent Method Using super()
# Problem Statement: Write a Python program where a Vehicle parent class 
# has a seating_capacity() method that accepts a capacity argument. 
# Create a Bus child class that overrides this method to provide a default 
# seating capacity of 50, 
# using super() to call the parent’s version internally.


"""
class Vehicle:
    def seating_capacity(self, capacity):
        print(f"Seating Capacity: {capacity} passengers")

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        super().seating_capacity(capacity)

bus1 = Bus()
bus1.seating_capacity()
"""