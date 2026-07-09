"""# Abstraction

from abc import ABC,abstractmethod


class BankApp(ABC):
        
    def database(self):
        print("Connected to database")

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        print("Login into mobile.")

    def security(self):
        print("Your mobile is Secured")

    def display(self):
       print("This is a display")


mobile = MobileApp()
mobile.security()
mobile.database()
mobile.display()

"""


# Abstraction
# --> Abstraction basically means hiding the complex implementation from the user.

#

"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass

class B(A):
    def show(self):
        print("Hi A")

obj1 = B()
obj1.show()
"""

from abc import ABC,abstractmethod

class Telpay:
    def pay(self):
        print("Paying using Telpay")

class Razorpay:
    def pay(self):
        print("Paying using RazorPay...")

class Purchase:
    def __init__(self,gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checking out...")
        self.gateway.pay()

gateway1 = Razorpay()
purchase = Purchase(gateway1)

gateway2 = Telpay()
purchase = Purchase(gateway1)
purchase.checkout()

print('HI')