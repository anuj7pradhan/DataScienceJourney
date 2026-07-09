# # Function: Reusable block of code
#     # Use 
#         # Code reusable
#         # Increase modularity
#         # Increase readability

# Syntax

# def function name(parameter):
# block of code
# function _name()

def Student():
    print("This is me XYZ")
Student()
Student()

print()

def Student(name):
    print("This is me", name)
Student("ANUJ")
Student("Pramila")

print()

# Return function
def add(a,b):
    return a + b
print(add(4,5))

#. Add function
x = add(4,5)
print(x)


# Task

# Even odd
def Even(num):
    if num % 2 == 0:
        print("Even", num)
    else:
        print("Odd",num)

num = int(input("Enter number: "))
Even(num)



def Calculation(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
operator = input("Enter operator: +, -, *, /:")

Calculation(num1, num2, operator)


# Palindrome

# dad

def check_palindrome(string):
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
check_palindrome("dad")



# Types of parmeter and argument in function

# 1. Positional argument: 
# 2. Keyword argument:
# 3. Default argument:
# 4. args
# 5. kwargs


# 1. Positional argument: 

def great(male, female):
    print(f" {male} is favulous")    
    print(f" {female} is favulous")
great("Sujan", "Siya")
great("Anuj", "Pramila")
great("Anjal","Prati")

# 2. Keyword argument:

def great(male, female):
    print(f"{male} is fav")
    print(f"{female} is fav")
great(female="Sajani", male="Sajan")
great(male= "Saroj", female="yabina")

def info(age,name):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
info(12,"Swostik")

info(name="Sworaj", age=23)

info("ANC", "bcd")

# 3. Default argument:

def great(name = "Guest"):
    print("Hello",name)
great("Ram")
great()


# default value should be placed at last
def great(sir, name= "sujan"):
    print("Hello", name)
    print("Hello", sir)
great("ram")


# Args: Handles multiple positional arguments
# by *
#. Stores in form of Tuple

def show(b,c,d,*a,e=3):
    print("a:",a)
    print("b:",b)
    print("c:",c)
    print("d:",d)
    print("E:",e)
show(1,3,2,4,6,4,5)


# kwargs: handles multiple keyword arguments
# by **
# store in form of dictionary

def show(**info):
    print(info)
show(name = "Sujan", age = "21",location ="Bhaktapur", subject = "python")
show(location ="Bhaktapur", subject = "python")

def Vat(*a, vat=13):
    total = sum(a)

    return total + (vat/100 * total) 

print(Vat(100,100,100))