# from abc import ABC, abstractmethod

# class Office(ABC):
#     @abstractmethod
#     def salary(self):
#         print("You get salary")

# class Workers(Office):
#     def bonus(self):
#         print("You get bonus")
#     def salary(self):
#         return super().salary()

# staff = Workers()
# staff.bonus()
# staff.salary()

    
"""
Exercise 1. Arithmetic Product and Conditional Logic

Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, 
return their product; otherwise, return their sum.
"""

def sum_mul(num1, num2):
    product = num1 * num2

    if product <= 1000:
        print(product)
    else:
        print(num1 + num2)

result =  sum_mul(40,30)
print(result)