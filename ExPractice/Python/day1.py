# Welcome to my python journey Day 1
print("Hello world")

x = 23
y = 34
print("This is the sum of x and y",x+y)

A = "Anuj"
a = 24

# a and A are different variables
print(A)
print(a)

#Camel Case = myCamelCase " each word, except the first, starts with a capital letter."
#PascalCase = MyPascalCase " each words including the first starts with a capital letter."
#snakecase = my_snake_case " each words are separated by the underscore ("_")"


# Arithematic Operations
a = 10
b = 3

sum = a + b
print("This is the sum of a and b", sum)

difference = a - b
print("This is the difference of a and b", difference)

multiplication = a * b
print("This is the multiplication of a and b", multiplication)

mod = a % b
print("This is the mod of a and b", mod)



'''Practice Problem: 
Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, 
return their product; otherwise, return their sum.'''

a = int(input("Enter a num a: "))
b = int(input("Enter a num b: "))
num = a * b
if num <= 1000:
    print("This is the multiplication", num)
else :
    print("This is the Sum",a + b )


"""
https://youtu.be/017gSDbZ4pQ
"""
import random

def numbers_game():
    answer = random.randint(0,100)
    
    while True:
        user_guess = int(input("What is your guess? > "))
        if user_guess == answer:
            print(f"Correct! The answer is {user_guess}")
            break

        if user_guess < answer:
            print(f'{user_guess} is too low!')
        else:
            print(f'{user_guess}is too high!')
numbers_game()