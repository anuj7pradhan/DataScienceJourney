# Functions

    # A function is a block of code that performs a specific task.
    # You can use it whenever you want by calling its name, which saves you from writing the same code multiple times.
# Benifits of using Function:   Increase code Readability & Reusability.

# Basic Concepts:
    # Create fiunctionn: Use the def keyword to define a function
    # Call function: Use the function's name followed by () to run it.
    # Parameter: THe variable listed inside parentheses in a function definition.
    # Argument: The actual value you pass to function when you call it.


# Types of Functionns:
    # 1. Built-in library function:
        # print(), input(), type(),sum() , max() etc.
    # 2. User-defined function:
        # Create your own function based on requirement

# Syntax
# def my_function(param):
#     instruction-1
#     instruction-2
# return result


# Example 1
# Create a function without parameters

def greetings():
    print("Welcome to python")

# Use or call this Function
greetings()

# Example 2
# Create a function with parameters
# fuction to add two numbers and print the result
def add2numbers(a,b):
    result = a + b
    print(f"The sum of {a}+ {b} = {result}")
# Calling this function with arguments
add2numbers(2,5)

add2numbers(a = 12, b = 30)

add2numbers(b = 2, a = 7)

print()

def add2numbers(a,b,c):
    result = a + b + c
    print(f"The sum of {a}+ {b}+ {c} = {result}")
# Calling this function with arguments
add2numbers(2,5,19)

add2numbers(a = 12, b = 30, c= 12)

add2numbers(b = 2, a = 7, c =30)


# Return Statement
    # It is used in a function to send a result back to the place where the function was called. 
    # When return is executed, the function stops running and immediately returns the specified value

# Ex. 
def add(a,b):
    return a + b # This line sends back sum of a and b
result = add(3,4)
print(result)



# function with return statement

def add2num(a,b):
    return a + b
    # return a - b  after return statement, function ends
sum2num = add2num(10,100)
print(sum2num)


# Ex. 3
# function to convert Celsius into Fahrenheit
# With return function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
temp_f = celsius_to_fahrenheit(25)
print(temp_f)
print(type(temp_f))

# Without return
# A bad practice Because it returns the NoneType datatype

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)
temp_f = celsius_to_fahrenheit(25)
print(type(temp_f))


# The pass statement
    # The pass statement is a placeholder in a function or a loop.
    # It does nothing and 
    # is used when you need to write code 
    # that will be added later or 
    # to define an empty function.
def my_function():  # Code to be updated later
    pass    # This does nothing for new
print("Hello, i just pass")



    # WAP to build a simmple calculator

# 3 steps to build calculator
    # 1. Functions for operations
    # 2. User input
    # 3. print result

#  Step 1 - Create function
# Function to add two number
def add(num1,num2):
    return num1 + num2

# Function to sub two number
def sub(num1,num2):
    return num1 - num2

# Function to multiply two number
def multiply(num1,num2):
    return num1 * num2

# Function to divide two number
def devide(num1,num2):
    return num1 / num2

# Function to average two number
def avg(num1,num2):
    return (num1 + num2)/2
#  Step 2 - user input
print("Please select a operation: \n "\
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n" \
        "5. Average\n")
select = int(input("Select a operation from 1,2,3,4,5:  "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second nummber: "))

# Step 3: Print the result

if select == 1:
    print(number1,"+",number2,"= ",  \
          add(number1,number2))
elif select == 2:
    print(number1,"-",number2,"= ",  \
          sub(number1,number2))
elif select == 3:
    print(number1,"*",number2,"= ",  \
          multiply(number1,number2))
elif select == 4:
    print(number1,"/",number2,"= ",  \
          devide(number1,number2))
elif select == 5:
    print("(",number1,"+",number2,")","/","2","=", \
          avg(number1,number2))
else:
    print("Invalid operation! Please select again!!!")