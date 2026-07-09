# Strings in python
    # A string is a sequence of characters. in python, strings are enclosed within single(') or double(")or triple(""")quotation marks.

# Ex.
print('Hello')  # use type() to check the data type
print("I won't give up.")
print('''"Quotes" and 'single quotes' can be tricked.''')
print("\"Quotes\" and 'single quotes' can be tricked")

# Formatted String

    # A formatted string in python is a way to insert variables or expressions inside a string. It allows you to format the output in a readable and controlled way.
    # There are multiple ways to format strings in python
        # 1. Old-style formatting (% operator)
        # 2. str.format() method
        # 3. F-strings (formatted string literals)
    #  Syntax "string % value" 
# Ex. 1. Formatted Strings - insert variables or expressions
# 1. Old style formatting - % operator
name = "Anuj"   #Creating a string
age = 23
print(type(name))   # Checking datatype
print(type(age))
print("My name is %s and I'm %d years old." % (name,age))
# %s, %d are placeholders for strings and integers.


#  2. Formatted String - str.format()
    # str.format() method
    # In python 3, the formmat() method is more powerful and flexible than the old-style % formatting.

    # SYNTAX
    # "string {}".format(value}
    # Ex.   
name = "Anuj"   #Creating a string
age = 23
print(type(name))   # Checking datatype
print(type(age))
print("My name is {} and I'm {} years old." .format(name,age))

# You can also reference the variables by index or keyword
print("My nme is {0} and I am {1} years old.".format(name,age))
print("My nme is {1} and I am {0} years old.".format(name,age))

print("My name is {name} and I'm {age} years old.".format(name = "Prativa", age = 28))


# 3. Formatted String - F Strings
    # In python 3.6, F-strings are the most concise andd efficient way to format stings.
    # You prefix the string with an f or F, and variables or expressions are embedded directly within curly braces{}.
   
    # SYNTAX
    # f"string {variable}"

# Example.
name = "Anuj"   #Creating a string
age = 23
print(type(name))   # Checking datatype
print(type(age))
print(f"My name is {name} and I'm {age} years old.")



# Escape Characters
    # Escape characters in python are special characters used in strings to represent whitespace, 
    # symbol, or control characters that would otherwise be difficult to include.
    # An escape character is a backslash \ followed by the character you want to insert.

print('Hello \nWOrld')      # \n for new line
print('Hello \tWOrld')      # \t for tab
print("\"Quotes\" and 'single quotes' can be tricky")   # print single and double quotes.

# String Operators
    # a = "Hello", b = "Python"  
"""
+   -> Concatination - Adds values on either side of the operator           a + b -> HelloPython
*   -> Repitition   - Creates new strings, concatinating multiple copies of the same string     a * 2 -> HelloHello
[]  -> Slice        - Gives the character from the given index
[:] -> Range Slice  -  Gives the character from the given range
in  -> Membership   - Returns true if a characer exists in the given string.
not in  -> Membership - Returns true if a characer does not exists in the given string.
r/R     -> Raw string - Suppresses actual meaning of Escape characters.
%       -> Format   - Performs String farmatting
"""
a = "Hello"
b = "Python"
print(a + b)    # Output: HelloPython

print(a * 2)    # Output: HelloHello

print(a[2])     # Output:l

print(a[1:3])   # Output: el

print("H" in a) # True

if "H" in a:
    print("Yes")
else:
    print("Noo")


print("J" not in a) # True

if "J" not in a:
    print("Yes")
else:
    print("Noo")

print(r"Hello\nWorld")  # Raw String: Supress the escape character

