# While loop in Python
# #Introduction
# While loop is used to execute a block of code repeatedly as long as a condition is true
# Syntax
# 
# while condition
#   Statement
# Ex
i = 1
while i <= 5:
    print(i)
    i += 1


i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
    print()

print("Even number in between 1 - 30")
i = 1
while i <= 30:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

print("Odd number in bet 1-30")
i = 1
while i <= 30:
    if i % 2 != 0:
        print(i, end = " ")
    i +=1
print()

i = 1
while i <= 6:
    print(f"{i} Anuj")
    i += 1
print()

i = 1
sum = 0
while i <= 5:
    sum += i
    i += 1
print(f"sum is {sum}")


i = 1
mul = 1
while i <= 5:
    mul = mul * i
    i += 1
print(f"multiplication is {mul}")


i = 1
num = int(input("Enter number: "))
while i <= 10:
    print(num, "*", i , "=" , num * i )
    i += 1










