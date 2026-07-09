# input() method
# Problem with the input() Method
    # Returns input from the user as a string

# used to take input from the user
# User input is always converted to a string

# input() method

name =input()
print(name)
print(type(name))


# input() Method with a message

number =input("Enter number: ")
print(number)

print(type(number))


# Typecasting the user input
# Typecasting is needed to convert a string to an integer
# input() method can be provided as an argument to the int() method

num = int(input("Enter a number:"))
print(num)
print(type(num))

numbers = input("Enter a numbers:")
print(type(int(numbers)))

n = int(input("Enter a list of numbers:"))

numbers =[]
for i in range(n):
    x = int(input())
    numbers.append(x)
print(f"Your list is {numbers}")