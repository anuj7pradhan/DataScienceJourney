# Abstract class: A class that cannot be instantiated on it's own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation.
#                 Abstract classes benifits:
#                 1. Prevents instantiations of the class itself
#                 2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod          #abc stands for "abstract base clas"


class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car.")

    def stop(self):
        print("You stop the car.")

"""vehicle = Vehicle()  # Can't instantiate abstract class Vehicle without an implementation for abstract methods 'go', 'stop'"""
car = Car()             # Can't instantiate abstract class Car without an implementation for abstract methods 'go', 'stop'
car.go()
car.stop()


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle.")

    def stop(self):
        print("You stop the motorcycle.")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()


class Boat(Vehicle):
    def go(self):
        print("You sail the boat.")
#  Can't instantiate abstract class Boat without an implementation for abstract method 'stop'

# So we have to def stop funtions too
    def stop(self):
        print("Ypu anchor the boat.")
boat = Boat()
boat.go()

boat.stop()