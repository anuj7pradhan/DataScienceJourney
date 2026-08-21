print("Hello World")
# This is comment that i am writing, a sinngle line comment
# comment helps us to explain the code that we wrote, it makes us understandable,
# filters the data
# readable
# professional
# 1. Create User Name
# 2. Print Message to the User
# 3. give Output to the User
# Store the final exam score
x = 100

x = 90 #Final exam score THis is inline comment

#Comments
# Comments are notes in code
# Python skips the comments
# Comment make code:
# Understandable , readable , professional 


# print function
##### a print function is the built_in Python function that dispalys messages on the output screen to communicate with  user

##### Function is [built-in, input,Len, ect are functions]
print("Hello dear")
print('Hi Python')
#   print("HELLO')
print("-----------------------------")
print("    Great LEARNING")
print("-----------------------------")

#### Escape Sequence
#Normal Characters : A-Z, a-z, 0-9, @ ,?
#Special character : \" \', \\, \n, \t
print("Hello \"Python\"")
print("Hi,\'Python'")
print("Path: C:\\Users\\Anuj")
# Adds a new line,it moves the text that comes after it to the next line
print("-----------------------------")

print("Message1\n")

print("Message2")

print("-----------------------------")

print("Message1\n\n\nMessage@")
print("-----------------------------")

print("Message1\tMessage2") #\t make a tab 
# Use print() to recreate this exact output 
# You are allowed to use only one PRINT()

# Your Learning Path:
#     - Python Basics
#     - Data Engineering
#     - AI
print("Your Learning Path:\n\t- Python Basics\n\t- Data Engineering\n\t- AI")
print("""Your Learning Path:
\t- Python Basics
\t- Data Engineering
\t- AI""")
price_shirt = 2500.00
price_jeans = 4500.00

qty_shirts = int(input("Enter no. of shirts"))
qty_jeans = int(input("Enter no. of jeans"))

total_shirts = price_shirt * qty_shirts
total_jeans = price_jeans * qty_jeans

sub_total = total_shirts + total_jeans
print("sub_total: ",sub_total)

discount = sub_total * 0.10
print("Discount: ", discount)

final_total = sub_total - discount
print("Final_price: ", final_total)
# RECAP
# print()
# Built-in function
# Displays the message in output for users
# USE  CASES:
    # Communicate, Show Results, Debugg,Test
# VARIABLES
#Variable is used to store/assign the value that the user wants
x=1
print(x)
x = 100
print(x)
#Values are manually fixed
print("My name is Anuj")
print("Anuj is learning Python")
print("Anuj wants to become Python expert")

#now lets assign the variable
name = "Anjal"
print("My name is",name)
print(name,"is learning Python")
print(name,"wants to become Python expert")

name = "Anuj"

# full control on variable
name = "Max"
language = "Java"

print("My name is",name)
print(name,"is learning", language)
print(name,"wants to become", language, "expert")
#RECAP

#Variables
# Make programs Dynamics
# Name to store a value
# Store in memory
# Reusable anytime
# updatable anytime
# - print the following three lines
# - add a variable to make it dynamic.

# info@datawithanuj.com
# support@datawithanuj.com
# www.datawithanuj.com
data_name = "datawithanuj"
print("info@",data_name,".com\nsupport@",data_name,".com\nwww.",data_name,".com")
# INPUT() function
# used to get info for something

# Using input() alone reads the user's response but immediately discards it.
# To keep the value, assign it to the variable
input("What's up?")
name = input("Enter your name")
age = input("Enter your age")
country = "Nepal"

print("Your name is", name)
print("You are",age, "years old.")
print(name,"came from", country)


# input() makes your programm more interactive
# input lets your program ask questions
# and react to what the user types, making it feel alive
# Data Types
# Data types
# a value determines the data type
# primitive data types: integer, string, boolean , float, 
# list, dict, tuple, set etc

a = 10
b = "anjal"
c = True

print(a,b,c)

print("a is ",type(a))
print("b is ",type(b))
print("c is ",type(c))

a = "anjal"
b = "ansh"
c = "pradhan"

print(a,b,c)
print(a+b+c)
#Data Types
a = 10 #int
b = 3.43 #float
c= "hello dear" #str
d = 'hi' #str
e = "342" #str
f = True #bool... : Boolean: can be either true or false
g = False #bool... : Bolean is used to handle logic and decision-making
h  = None # NoneType means "no-value", "nothing", or "unknown", It's used to show the absence of any data
i = "" # Blank data-type is a string data-type, Blank "" is a string value with no characters inside, it is not same as None
j = " " # str  - Empty Space, a space in between Double Cotes " "

# Standalone Functions -- print(), type()...
# Methods of class -- upper(),replace()...
#Operations -- + , / , < , >, ==, in or

#Standard Library :-- Built in module, python uses to call different standard functions
#3rd party functions :-- Pandas, NumPy, TensorFlow etc.
#User Defined function :-- 
# syntax for function
# function_name(value)
print("hi")
type(58)


# syntax for methods
# value.method_name()

"hello".upper()
#50.bit_length()

text = "hi"
number = 23
print(text)
print(number)

type(text)
type(number)

# type() returns the data type of a value so youknow what kind of object it is.

print(len(text))
# print(len(number))

print(text.upper())
# number.upper()
print(number.bit_length())
# print(text.bit_length())
# Each value has a datatype
# it automatically detects data type
# Dynamic: Data Types can change anytime
# 3 Categories
    # No Value: None Type
    # Single Value: int, str, bool, float, complex
    # Multiple Values: set, tuple, dict, list
#Values are objects of a data type class
        # Create 5 variables - each with a different data types:
        # 1. Your age
        # 2. Your height(with decimals)
        # 3. Your name
        # 4. Are you a student?
        # 5. Something with no value yet
        #    Then print the values , data types,lengths of all variables
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
name = input("Enter your name: ")
question = input("Are you a sutdent?")

print(age, height, name, question)

print(type(age))
print(type(height))
print(type(name))
print(type(question))

#print(len(age))
#print(len(height))
print(len(name))
# Chapter 8
### String Function
#Types
name = "Anuj"
print(type(name))

age = 23
print(type(age))

print("Your age is: ",age)
print("Your age is: "+str(age))

age = age + 9
print(age)

#Change the  data type to string
age = str(age)
print(type(age))
#Math
password = "123ab"
print(len(password))


text = """
Python is easyto learn.
Python is powerful.
Many people love python.
"""

#Python and python are two different terms
print(text.count("Python"))

#DEBUG the code searching the special characters
print(text.count("$"))



#"2026/08/08"
#Change the / with -

date= "2026/08/08"

print(date.replace("/","-"))

phone = "977-9843-03-46-47"
print(phone.replace("-","/"))
print(phone.replace("-",""))
price = "$1,200.89"
print(price.replace("$","").replace(",",""))
#Python Challenge
# Convert the messy phone number into a clean number format with only digits. "+49 (176) 123-4567"
phone_num = "+49 (176) 123-4567"

print(phone_num.replace("+","00").replace(" ","").replace("(","").replace(")","").replace(" ","").replace("-",""))
#Join Text
first_name ="Anuj"
last_name = "Pradhan"

full_name = first_name +" "+ last_name
print(full_name)
#Transformation
folder = "C:/User/Anuj/"
file="report.csv"

full_file_path = folder + file
print(full_file_path)
# f-string
# modern, super_easy way to format and build strings 
# "f" stands for "formatted"
# lets you easily put variables and expressions directly inside string value
name = "ANUJ"
age = 33
is_student = False

print("My name is " + name + ", and I am " + str(age) +" years old, and student status is " + str(is_student)+".")
print(f"My name is {name}, and I am {age} years old, and student status is {is_student}.")

#f-string is : Shorter,Cleaner, Easier to read.

print(f"2 + 3 = {2 + 3}")
print(f"{{This is me}}")
#Transformation
stamp = "2026-08-08 13:12"
print(stamp.split(" "))

stamp = "2026-08-08"
print(stamp.split("-"))

csv_file = "123,Max,UK,2026-08-08,M"
print(csv_file.split(","))
# String Repitition

print("ha " * 5)
print("===============")
print("=" * 35)
print("*" * 35)
#Indexing and slicing

extract = "hello"
# [Start:End:Step]
# Start is included but End is not included

print(extract[0:1])
print(extract[1:4])
print(extract[0:4])
print(extract[-5:])

# [Start:End:Step]
print(extract[0:5:2])



#Indexes and slicingtext ="Python"

#Extract the first character

print(text[0])
print(text[-6])

#Extract the last character
print(text[-1])
print(text[5])

#Extract h
print(text[3])
print(text[-3])

date = "2026-09-19"
#Extract the year
print(date[0:4])
print(date[:4])
print(date[:-6])
print(date[-10:-6])

#Extract the Month
print(date[5:7])
print(date[-5:-3])

#Extract the Day
print(date[8:])
print(date[-2:])

#Cleaning
## Data Cleaning
#Remove Spaces
#lstrip()
#rstrip()

#strip()

# lstrip() function removes the left white spaces only
text= " Engineering"
print(text.lstrip())

# rstrip() function removes the right white spaces only
text= "Engineering "
print(text.rstrip())

text= "    Engineering ".strip()
print(text)

#strip() function removes the left and right whitespaces only
text = "Data   Engineering  ".strip()
print(text)

# pass the value in the strip() function
text = "###ABC###"
print(text.strip("#"))

# USE CASE - Detect extra spaces
# check the length before and after strip() to find the unwanted spaces
# len() function is used to count the no. of characters
text = " ANJALANSH"
print(len(text))
print(len(text.strip()))

no_of_spaces = len(text) - len(text.strip())
is_clean=len(text) == len(text.strip())

print("n0_of_spaces:",no_of_spaces)
print("Is my data clean?",is_clean)
### CASE CONVERSION
#Case Conversions

# upper() method changes the value into upper case
text = "PythoN ProgramminG"
print(text.upper())

# lower() method changes the value into lower case
print(text.lower())



# Chapter 9
# Math functions
# Number types functions

x = 5
y = 5.4
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

print(float(x))

x = "32"
print(type(x))
print(x * 8)

# change the string value into integer
# int() function converts compatible value into int value
x = int(x)
print(type(x))

print(x * 8)
x = 3.14

print(int(x))

print(float(x))
x = 3  #real
y = 32 #imaginary

print(complex(x,y))
# Numbers  
# Math Operator
print(2+3)
print(2-3)
print(2*3)
print(45/6)
print(43//3) # // Floor division It divides two numbers and rounds down
print(7%5) # Remainder  - The leftover part after division - used to check if a number is even
print(2 ** 3) #  here 2 is the base and 3 is the exponents,Exponentiation - It raises a number to the power of another number

x = 2
#x = x + 3
x +=3
print(x)

x -= 2
print(x)

x *= 2
print(x)


## Number function
# Round 
import math # Math module is imported
#Measuring distance

print(abs(2 - 10)) # useful for measuring the distance, or size, regardless of direction

#Rounding Numbers
price = 35.2342382342345

# round() function is handy in data analysis to clean numbers for reports or save space
print(round(price))
print(round(price,2))
print(round(price,1))

print(math.floor(price)) # floor() function
print(math.ceil(price)) #ceil() function is  perfect for data engeneering - like splitting data into pages or batches

print(math.trunc(price))
print(int(price))

### Number functions #Random
import random

#Random sampling = picking a smaller,random part of a huge dataset

print(random.random())
print(random.randint(1,10))

### Validation
#Check if numbers are truly whole floats with .0 might just be from file exports

x = 32.0
print(x.is_integer())

y = 34.2
print(y.is_integer())


x = 70.3
print(isinstance(x,int))

print(isinstance(x,float))

# Challenge
#### Generate a random integer between 1 and 100, and check if the result is even number?
import math
import random
rand = random.randint(1,100)
rand
if rand % 2 == 0:
    print(rand, "is even")
else:
    print(rand, "is odd")
# Chapter 10
## Conditional Statement
## if , else, elif
# CONTROL FLOW
# Conditional Statements -> if,  else, elif

# Loops Types = for , while
    # -> Loops Control  = break, pass continue

# Boolean Expressions
    # Values = True , False
    # Functions = bool(), any(), all(), isinstance()
    # Comparision Operators = ==, !=, <, >,<=, >=
    # Logical Operators  = and, or, not
    # Membership Operators = in, not in
    # Identity Operators = is, is not


###Chapter 11
print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))
email =  ""
phone=  "977-123456789"
username = ""
#Allows registration
# if any field is filled
print(any([email, phone, username]))

#Allows registration
# only if all field is filled
print(all([email, phone, username]))
print(isinstance(123, int))
print(isinstance(True, str))
print("Hello".endswith("o"))
print("Hello".startswith("o"))
# Course 12
## Python Comparison Operators
print(10 == 10)
print(10 != 9)
print(8>4)
print(9>=9)
print(2<9)
print(4<=4)
print("a" < "b")
print("a" > "b")
print("a" == "A")
#Chained operator
print(1 < 3 < 8 >  5  == 6)
# Chained comparison work like SQL's BETWEEN They check if a value is between two bounds
# Is age bet 18 and 30?
age = 45
print(18 <= age <=40)
# Course 13
## Python Logical Operators
#Condition 1 and condition 2
#Logical Operation
print(3 > 1 and 4 > 2)

print(3 > 1 and 4 < 2)
print(3 > 1 or 4 > 2)
print(3 > 1 or 4 < 2)
# Checks if the system is under pressure

cpu_usage = 80
memory_usage = 97
print(cpu_usage > 90 or memory_usage >90)

cpu_usage = 70
memory_usage = 77
print(cpu_usage > 90 or memory_usage >90)

# Check user credentials before login
email = True
password = False

print(email and password)
print(email or password)
# Logical operator NOT
print(4 > 4)
print(3 != 4)
print(not True)
print(not False)
print(not not False)
name = " "
print(not name)
print(not 0 )
# Control Mixed Conditions
print(5 == 5 or 7 > 5 and 6 < 4)
print((5 == 5 or 7 > 5) and 6 < 4)
# Question
# Allow access only if the user is logged in or they are guest 
# but they must not banned
is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest) and not is_banned)
# Python  Challenge
# Check if user's name is not empty and the age is greater than or equal to 18
username = ""
age >= 18

print(any([username, age]))

# Check if the password ia at least 8 characters long and does not contain spaces
password = "Abcd e32f"
print(all([password]))
# Check if a user's email is not empty. contains '@' and ends with '.com'

# Check if a username is a string, is not none, and is longer than 5 characters

# Check if the user is either an admin or a moderator, and either they're not banned or they've veified their email

print("Hello it's me {} and i am from {}.".format("Anuj","Kirtipur"))




