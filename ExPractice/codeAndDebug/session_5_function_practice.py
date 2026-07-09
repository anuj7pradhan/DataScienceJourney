# # # # What is a Function?
# # #     # A function is a reusable block of code that performs a specific task. 
# # #     # Instead of writing the same logic again and again, 
# # #     # You write it once inside a function 
# # #     # and call it whenever you need it.
# # # # This follows the DRY principle - Don't Repeat yourself
# # # # It is one of the most important principles in programming.

# # # # Function also make your code easier to read, easier to debug, and easier to maintain.
# # # # If the logic needs to change, you change it in one place not everywhere.

# # # # Syntax
# # # # def function_name():
# # #     # code goes here
# # # # calling_a function
# # # # function_name()

# # # # Ex.
# # # print("Good morning")
# # # print("This is afternoon")
# # # print("Good bye")

# # # print("Good morning")
# # # print("This is afternoon")
# # # print("Good bye")

# # # print("Good morning")
# # # print("This is afternoon")
# # # print("Good bye")

# # # print("Good morning")
# # # print("This is afternoon")
# # # print("Good bye")

# # # print("Good morning")
# # # print("This is afternoon")
# # # print("Good bye")


# # def greet():    # This is a function
# #     print("Good morning")
# #     print("This is afternoon")
# #     print("Good bye")

# # greet() # This is Calling a function
# # greet()


# def odd_even():
#     num = int(input("Enter number:"))
#     if num % 2 ==0:
#         print("Even")
#     else:
#         print("Odd")

# odd_even()

# Q.    Write a function that prints all the factors of a number entered by user.

# def print_factors():
#     num = int(input("Enter a number: "))
#     for i in range(1, num):
#         if num % i ==0:
#             print(i, end=" ")

# print_factors()

# Parameters and Arguments
    # A parammeter is a variable listed inside the function definition.
    # An argument is the actual value you pass when calling the function.
    # Parameters make functions flexible- the same function can work eith different data everytime.
# def greet(name): # name is the parameter
#     print(f"Hello, {name}")
# greet("Shyam")  # Shyam is argument
# greet(f"Sunchakachak")  # Sunchakachak is argument




# 3 int as a parameter, print the total

# def addition(a,b,c):    #Parameter
#     ans = a + b + c
#     print(f"{a} + {b} + {c} = Total: {ans}")
# addition(12,2,14)   # Arguments

# addition(1,2,3)

# Q. Ask a name,age, gender, and print using function

# def info(name, age, gender):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Gender: {gender}")
# info("Anuj",30,"Male")
# info("Prativa",29, "Female")
# info("Ashu", 4, "Male")

# 4:03