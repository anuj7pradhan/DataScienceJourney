# Arguments in Functions
    # Argumments are the values that are passed into a function when it's called.
    # A function must be called with the right number of arguments.
    # If a function has 2 parameters, you must provide 2 arguments when calling it.

# Ex.   function defined one parameter (variable)
def greetings(name):    # here: name is parameter
    print("Hello," + name + "!")
greetings("Anuj")   # here: Anuj is argument
greetings("Anjal")  # here: Anjal is argument

# Types of function Arguments

    # 1. Required arguments (Single/Multiple arguments)
    # 2. Default arguments
    # 3. Keyword arguments (named arguments)
    # 4. Arbitrary arguments (variable-length arguments *args / ** kwargs)


# 1. Required arguments (Single/Multiple arguments)
def greeting(name): # name is parameter
    print(f"Hello, {name} it is from required argumments")
greeting("Suresh") # Suresh is argument
# greeting()  # required an argument to run code

def intro(course_name, instructor_name):    # Multi parameter
    print(f"I am learning {course_name} and {instructor_name} is my instructor.")
intro("Python","Pramila") # Multi arguments
  
  
# 2. Default arguments

def greet(name =  "World"):  #World is a default value
    print(f"Hello, {name}!!!")
greet() # Runs without error using default value

greet("Hello")  # Argument passed by force.



# 3. Keyword arguments (named arguments)

def divide(a,b):
    return a/b
result1 = divide(100,20)    #Positional argument
print(result1)

result2 = divide(a = 100,b = 20)
print(result2)

result3 = divide(b = 20,a = 100)
print(result3)


# 4. Arbitrary arguments (variable-length arguments *args / ** kwargs)

    # If you're unsure how many arguments will be passed, use *args to accept any number of posiotional arguments.
    # Purpose: Allows you to pass a variable number of positional arguments.
    # Type: The arguments are stored as a tuple
    # Usage: Use when you want to pass multiple values that are accessed by position.

# Ex1.
def add_numbers(*args):
    return sum(args)
result = add_numbers(1,2,3,4,5,6,7,8,9,10)     # Any numbers of argument
print(result)    # Output: 55


# Ex. on Arbitrary Arguments (*args)

def add2numbers(a,b):
    return a+b
result = add2numbers(10,23)
print(result)


def add2numbers(a,b,c):
    return a+b+c
result1 = add2numbers(10,23,43)
print(result1)



# Stores numbers as Tuple
def add_numbers(*args):
    print(type(args))
    return sum(args)
results3 = add_numbers(1,2,3,4)  #Variable numbers of arguments
print(results3)


def greetings(*names):
    for name in names:
        print(f"Hello, {name}")
greetings("Simrik","Kritik","Pratik")



"""
Arbitrary Keyword arguments (**kwargs)
    If you want to pass a variable number of keyword arguments, use **kwargs.
    
    Purpose: Allows you to pass a variable number of keyword arguments (arguments with names).
    Type: The arguments are stored as a dictionary.
    Usage: Use when you want to pass multiple values that are accessedd by name.

    Ex.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Anuj",age = 32,location = "Ktm")

Note: Here,**kwargs takes in any number of keyword arguments and print each key-value pairs.

"""


# Arbitrary keyword arguments (**kwargs)
# Note: stores arguments as dictionary

def print_details(**kwargs):
    print(type(kwargs))     # Dictionary type
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name= "anuj",age= 21,city = "ktm")



def print_details(**kwargs):
    print(type(kwargs))     # Dictionary type
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name= "anuj",age= 21,city = "ktm",course = "Python")











