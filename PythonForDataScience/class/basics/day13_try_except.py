# Package in python
    # A collection of module is called package in python.
        # __init__.py
        # file1.py
        # file2.py

# Library
     # A collection of package is called library in python.




# Exception handling
    # 1. Syntax Keyerror
        # When we write code in wrong format or wrong way. It is detected by compiler or interpreter and it will not execute the program.

# print("Hello)   #SyntaxError: unterminated string literal (detected at line 15)

# 2. Logical Keyerror
        # When we write code in correct format but it gives wrong output.
        # It is not detected by compiler or interpreter and it will execute the program.

# a = 9
# b = 3
# print(a-b)

    # 3. Run Time Error
        # When we write code in correct format but it gives error during execution.
        # It is detected by compiler or interpreter and it will not execute the program.

# a = 23
# b = 0
# print(a/b) # ZeroDivisionError: division by zero
    # Types of Run time error
        # 1. ZeroDivisionError: division by zero
            #  When we divide a number by zero. 
            # It is detected by compiler or interpreter and it will not execute the program.
       
         # 2. Type error
# a = 23
# b ="a"
# print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# len(213) # TypeError: object of type 'int' has no len()

         # 3. Name error
# print(a) #NameError: name 'a' is not defined
        #


# Index error

# a = [12,3,4,5]
# # print(a[4]) IndexError: list index out of range

# Value error

# a = { 'name': "anuj", 'program': "python"}
# print(a['gender']) # KeyError: 'gender'


# Exception handling
    # Program crash hudaina
    # User friendly message dekhna sakincha
    # Bugs identify garna sajilo huncha
    # Application stable huncha


# Syntax

"""
try:
    risky code
except:
    error handling code
"""


# try:
#     print(19/0) # Risky code 
# except:
#     print("Cannot divide by zero")  # Warning dine

"""

try:
    risky code
except:
    handle error
else:
    error nabhaye
finally:
    always execute

"""



# Ex.

# try:
#     num1 = int(input("Enter num1: "))
#     num2 = int(input("Enter num2: "))

#     result = num1 / num2
# except ZeroDivisionError:
#     print("Not divisible by zero")

# else:
#     print(f"The result: {result}")
# finally:
#     print("Thanks for participation")

# try:
#     num = 12
#     str = "abc"
#     result = num + str
# except TypeError:
#     print("Cannot cancatinate int to string")
# else:
#     print(result)
# finally:
#     print("thanks")



# # Value error

# try:
#     num1 = int(input("Enter num: "))

#     num2 = int(input("Enter num:"))

#     result = num1 + num2

# except ValueError:
#     print("This is a value error")

# else:
#     print(result)

# finally:
#     print( " Ypu learned Value error handling")



# Type error

# try:
#     num1 =int(input("Enter num1: "))
#     num2 = int(input("Enter num2: "))
#     result = num1 + num2
# except TypeError:
#     print("Enter numbers only")
# else:
#     print(result)
# finally:
#     print("Learned type error")



# Key error

# try:
#     learningpython = {"name":"learningpython","location":"abc"}

# except KeyError:
#     print("Key error")
# else:
#     print(learningpython.get("location"))
# finally:
#     print("Enjoy learningpython")




# Name Error

# try:
#     print(z)
# except NameError:
#     print("name error")
# else:
#     print(z)
# finally:
#     print("z is printed")


# try:
#     number = [1,2,3,4,5]
#     print(number[10])

# except IndexError:
#     print("Index error")
# else:
#     print(number)
# finally:
#     print("Numbers print garnu")

# try:
#     number = [1,2,3,4,5]
#     print(number[10])   # Risky code
# except:
#     print("hi") #Error handling code