# Encapsulation---> The repeating of the data and method with single unit
    # Hiding internal state object and restrict direct access from outside

# Why
# Data secure
# Data hiding
# Control access to the data


# Encapsulation is achieved by using access modifier
# private, protected, public accessifier
    # private ---> attribute and method are accessible only in that class
    # protected ---> attribute and method are accessible only in that class and subclass
    # public ---> attribute and method are accessible from outsiude the class

# Public encapsulation
"""
class Student:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"This is {self.name}")
        
st1 = Student("Pramila")
st1.show()

print(st1.name)

class B(Student):
    def display(self):
        print(f"This is display{self.name}")
    
b1 = B("Padamshree")
b1.display()
"""

# private accessfier: uses double underscores(__variable_name)
class Student:
    def __init__(self, name):
        self.__name = name
    
    def show(self):
        print(f"This is {self.__name}")
st1 = Student("Pramila")
st1.show()

# print(st1.__name) # cannot access outside the class and subclass

# class B(Student):
#     def display(self):
#         print(f"This is display{self.__name}")
    
# b1 = B("Padamshree")
# b1.display()



# Private accessifier in methods/ Imp one
"""

class Student:
    def __init__(self, name):
        self.name = name
    
    def __show(self):       # this is private accessifier in method using __method_name
        print(f"This is {self.name}")
    
    def display(self):
        self.__show()

st1 = Student("Pramila")
st1.display()

"""

# Task 1
# Create a Python class named ATM to manage a bank account using the Private Access Modifier.

# Requirements:
# Create a private attribute named __balance and initialize it using the constructor (__init__).
# Create a method named deposit(amount) that:
# Adds the given amount to the account balance.
# Displays the message "Deposit Successful".
# Create a method named withdraw(amount) that:
# Deducts the given amount if there is sufficient balance.
# Displays "Withdrawal Successful" if the transaction is successful.
# Otherwise, displays "Insufficient Balance".
# Create a method named show_balance() that displays the current account balance.
# Create an object with an initial balance of 10000 and perform the following operations:
# Display the current balance.
# Deposit 5000.
# Display the updated balance.
# Withdraw 3000.
# Display the final balance.
# Finally, try to access the private attribute directly using atm.__balance and observe the result
"""
class ATM:
    def __init__ (self, balance):
        self.__balance = balance
        # self.amount = amount

    def deposit(self,amount):
       self.__balance += amount
       print(f"Deposit successful")

    def withdraw(self,amount):
    
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")

        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

bl1 = ATM(10000)
bl1.show_balance()
bl1.deposit(5000)
bl1.withdraw(3000)
bl1.show_balance()
# print(f"{bl1.__balance}")

"""


# PROTECTED ACCESSIFIER
"""
class ATM:
    def __init__ (self, balance):
        self._balance = balance
        # self.amount = amount

    def deposit(self,amount):
       self._balance += amount
       print(f"Deposit successful")

    def withdraw(self,amount):
    
        if amount <= self._balance:
            self._balance -= amount
            print("Withdrawal Successful")

        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Current balance: {self._balance}")

bl1 = ATM(10000)
bl1.show_balance()
bl1.deposit(5000)
bl1.withdraw(3000)
bl1.show_balance()
print(f"{bl1._balance}")



print(bl1.__dict__)
"""