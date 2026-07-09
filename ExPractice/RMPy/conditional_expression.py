# Conditional Expressions

#    It provide a shorthand way to write simple if-else statements.
# Also known as Ternary Operator

# Syntax
    # value_if_true if condition else value_if_false


# Ex.
# age = 15
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# 5. Conditional Expressions (ternary Operator)

# age = 26
# status = "Major" if age >= 18 else "Minor"
# print(status)


# Ex. 1
# What is expected output and reason?
value = None

if value:
    print("Value is. True")
else:
    print("Value is False")

# Ex. 2

# Write a simple program to determine if a given year is a leap year suin a user input.

# Note: Leap year condition:
    # divisible by 4 but not by 100 unless it's 400

# year = int(input("Enter a year: ( e.e. 2026): "))

# # Condition leap year
# if (year % 4 == 0 and year % 100 != 0) or ( year % 400 == 0):
#     print(f"{year} is leap year.")
# else:
#         print(f"{year} is not a leap year.")

# Ex. 3

# Q. Login Authentication using conditional statement.
# Assume you have a predefined username and password.

# Write a program that prompts the user to 
# enter a username and password 
# and checks wheter they match.
# Provide appropriate messages for the following cases:
    # Both username and password are correct.
    # Username is correct but password is incorrect.
    # Username is incorrect.

# Predefined usernaem and password
predefined_username = "AnjalAnsh"
predefined_password = "pass123"


# prompts the user to enter a username and password 
username = input("Enter your username: ")
password = input("Enter password: ")

# username and password match
if username == predefined_username:
    if password == predefined_password:
        print("Both username and password are correct.")
    else:
     print("Username is incorrect.") 
else:
     print("Invalid Username.") 
# elif username == predefined_username or password != predefined_password:
#     print("Username is correct but password is incorrect.")
# else:
#      print("Username is incorrect.") 