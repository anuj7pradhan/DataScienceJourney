# Print all the numbers which are divisible by 3 and 5, from 1 to 100.

# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, end=" ")
#     i += 1


# Sum of all the numbers from 1 to 100.

# start = int(input("Enter num1: "))
# end = int(input("Enter num2: "))
# i = start
# sum = 0
# while i <= end:
#     sum += i
#     i += 1
# print(sum,end=" ")

# Sum of all numbers fromm 1 to 100 divisible by 2 and 7


# start = int(input("Enter num1: "))
# end = int(input("Enter num2: "))
# i = start
# sum = 0
# count = 0
# while i <= end:
#     if i % 2 == 0 and i % 7 == 0:
        
#         count += 1
#         sum += i
#         print(f"And they are {i}")
#     i += 1
# print(f"the sum is {sum}")
# print(f"there are {count} numbers that are divisible by 2 and 7")



# ask a number from the user, print the multiplication table upto 10.

# i = 1
# n = int(input("Enter number: "))
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i+=1


# Ask a number from the user, print all the factors.

# number = int(input("Enter number: "))
# i = 1
# while i <= number:
#     if number % i == 0:
#         print(i, end=" ")
#     i += 1


number = int(input("Enter number: "))
i = 1
count = 0
while i <= number:
    if number % i == 0:
        count += 1
        print(i, end=" ")
    i += 1
print()
print(f"Total factors of {number} are {count} ")