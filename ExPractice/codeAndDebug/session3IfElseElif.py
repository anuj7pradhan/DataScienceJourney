# Conditional statement
    # If it is raining, carry an umbrella, otherwise don't.
# Programs to make decisions and execute different code based of the condition is True of False

# IF Statement

# If the condition is True, the indentd blocks runs. If it is False, Python simply skips it.


marks = 75
if marks >= 40:
    print("You have passed.")


# IF-ELSE Statement

# Use else when you want something to happen when the condition is False.
# One of the two bolcks will always run-never both, never neither.

age = int(input("Enter your age: "))
 
if age >=18:
    print("You can vote.")
    print("You are eligible.")
    print("You are responsible voter.")
else:
    print("You cannot vote.")

#Ex 2

java = int(input("Ennter your Java marks: "))
python = int(input("Ennter your Python marks: "))

if java >= 40 and python >=40:
    print("You are passed")
else:
    print("You are failed")



# IF-ELIF_ELSE Statement
# When you have more than two possible outcomes, use elif
#Python checks each. condition from top to bottom and runs the first one that is True. The rest are skipped entirely.

day = input("Enter day: ")
if day == "sunday":
    print("School 1st day.")
elif day == "monday":
    print("School 2nd day")
elif day == "tuesday":
    print("School 3rd day")
elif day == "wednesday":
    print("School 4th day")
elif day == "thursday":
    print("School 5th day")
elif day == "friday":
    print("School 6th day")
else:
    print("Bida")

"""
90 and above -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
60 and below -> Fail
"""

marks = int(input("Enter marks: "))

if marks >=91 and marks <= 100:
    print("A")
elif marks >=81 and marks <=90 :
    print("B")
elif marks >=71 and marks <= 80:
    print("C")
elif marks >=61 and marks <=70:
    print("D")
elif marks >=0 and marks <=60:
    print("Fail")
else:
    print("Invalid marks")


"""
NESTED if-else statement
    You can place an if statement inside another if statement.
    This is called nesting and is useful when second condition
    only makes sense if the first one is already True.
"""

# Age >= 18
# Certificate -> True

age = 34
certificate = True

# if age >= 18:
#     pass
# else:
#     print("Cannot hire, age is less than 18.")

if age >= 18:
    if certificate == True:
        print("You will be hired.")
    else:
        print("Cannot hire due. to no certificate.")
else:
    print("Cannot hire, age is less than 18")


"""
Shorthand if-else (Ternary Operator)
"""

# Python lets you write a simple if-else in single line.
# This is called the ternary operator. It is useful when to assign a value based on a condition.

age = int(input("Enter age: "))

# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

status = "Adult" if age >= 18 else "Minor"
print(f"Your status is {status}")