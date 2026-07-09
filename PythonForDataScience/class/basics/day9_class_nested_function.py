# Global variable
#   it is defined Outside the function
#   Can be accessed all over the program
#   

# a = 100 # Global variable
# def student():
#     print(a)

# student()

# def display():
#     print(a)
# display()



# Local variable
#   it is decleared inside the function
#   accessed within the function


# def song():
#     b ="Nemath" # Local variable
#     print(b)
# song()


# def genre():
#     print(a)
# genre()


# # local variable is given priority
# def student():
#     a = 200
#     b = 28
#     print(a+b)
# student()


# name = "Anuj" # Global variable
# age = 22    # Global variable
# def info(): # Function
#     location = "Kirtipur" # local variable
#     print(f"My name is {name} i am {age} and i amm from {location}") # Reading the function
# info() # calling the function



# Nested function
# s_name ="Prakriti"
# course = "Python"
# def student():
#     print(s_name,course)
#     def area():
#         location = "bha"
#         print(location)
#     area()
# student()

# def a():
#     name = "Sweety"
#     print(name)
#     def b():
#         print(name)
#         print("learningpython")
#     b()
# a()

# def A():
#     x = 100
#     def B():
#         # nonlocal x
#         x+=5
#         print(x)
#     B()
# A()


# def Loopi():
#     for i in range(1,6):
#         print(i)
# Loopi()


# def Multi(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")
# n = int(input("Enter num: "))
# Multi(n)
# Multi(7)


    
    # Lambda function: anynomous function for calculation in single line
    # Syntax:
        # lambda variable: expression

x = lambda a,b: a+b
print(f"lambda function to add the variable: {x(3,4)}")

sq = lambda a: a*a
print(f"Lambda function to find the square: {sq(4)}")

add = lambda a,b: a+b
print(f"Lambda function to find theaddition: {add(12,12)}")

sub = lambda a,b:a - b
print(f"Lambda function to find the subtraction: {sub(12,3)}")