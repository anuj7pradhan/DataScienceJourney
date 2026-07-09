"""
Q7. Take a nummber as an input. Print whether it is positive, negative, or zero.
"""

num = int(input("Enter your number: "))

if num > 0:
    print("positive")
elif num < 0:
    print("Negatie")
else:
    print("Equal to Zero")


"""
Q8. Take two numbers as input. Print the greater of the two. If they are equal, print "Both are equal".
"""

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both are equal.")


"""
Q9. Take a student's marks as input. Print their grade based on this scale:

90 and above -> A
75 - 89 -> B
60 - 74 -> C
40 - 59 -> D
below 40 -> Fail
"""

marks = int(input("Enter your marks: " ))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 75:
    print("B")
elif marks >=60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")

"""
Take a year as input. Check if it is a leap year. 
A year is a leap year if it is divisible by 4, 
but not by 100, 
unless it is also divisible by 400.

200 - not leap year
204 - leap year
800 - leap year
"""
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leaaaap year.")


# 1:50:30