# # condition
# # based on condition it gives True or False value

# i = 10
# if i == 10:
#     print("Yes")


# # Syntax

# num = int(input("Enter num: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # Elif

# # Syntax

# # if condition:
# #     Statement
# # elif condition:
# #     statement
# # else:
# #     statement

# num = int(input("Enter num: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # Grading system: 

# grade=int(input("Enter marks: "))
# if grade >=90 and grade <= 100:
#     print("A")
# elif grade >= 80 and grade < 90:
#     print("B")
# elif grade >=70 and grade  < 80:
#     print("C")
# elif grade>=50 and grade < 70:
#     print("D")
# elif grade < 40 and grade >0:
#     print("Fail")
# else:
#     print("Invalid")

# Nested if: if statement inside another if statement


# num = int(input("Enter number: "))

# if num > 0:
#     if num % 2 == 0:
#         print("Positvive even number.")
#     else:
#         print("Positive odd number")
# else:
#     print("Negative")


# 18 - 60 -> adult voter
# 60 - 100 -> senior citizen
# <18 -> not eligible for vote
# < 1 and > 100 invalid age


# age = int(input("Enter age: "))

# if age >= 18 and age <= 100:
#     if age >=18 and age <= 60:
#         print("Adult voter.")
#     else:
#         print("Senior voter")
# elif age <18 and age > 0:
#     print("not eligible to vote")
# else:
#     print("Invalid age")

# 3 num 
    # Greater num find

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))

# if num1 > num2 > num3:
#     print(f"{num1} is greater than {num2} and {num3}")

# elif num2 > num3 > num1:
#     print(f"{num2} is greater than {num3} and {num1}")

# else:
#      print(f"{num3} is greater than {num1} and {num2}")


# 

num1  = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Select operator (+ ,- ,* ,/) : ")
# 

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator =="*":
    print(num1 * num2)

elif operator == "/":
    
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by 0")

else:
    print("invalid")