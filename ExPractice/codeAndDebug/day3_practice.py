# Q15. Print all the numbers which are divisible by 3 and 5, from 1 to 100.

i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1
print("The numbers which are divisible by 3 and 5 are all printed.")


# Q16. Sum of all numbers from 1 to 100.

total = 0
start = int(input("Enter start: "))
end = int(input("Enter end: "))
i = start
while i <= end:
    total += i
    i += 1
print(f"Sum of all numbers from 1 to 100 = {total}")

# Q17. Sum of all numbers from 1 to 100 divisible by 2 and 7.

start = int(input("Enter start: "))
end = int(input("Enter end: "))
i = start
total = 0
count = 0
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        total += i
        count += 1
        print(i)
    i += 1
print(f"The sum of all numbers is {total}")
print(f"Ther are {count} total nnumbers which is divisible by 2 and 7.")

"""
Q18. Ask a number from the user, 
print the multiplication table upto 10.
"""

num = int(input("Enter a multiplication: "))

i = 1
while(i<=10):
    print(f"{num} * {i} = {num * i}")
    i += 1


# Q19. Ask a number from the user, and print all the factors.

number = int(input("Enter number: "))
i = 1
while i <= number:
    if number % i == 0:
        print(i, end=" ")
    i += 1


# Q20. Ask a number from the user, and Count all the factors.

num = int(input("Enter number: "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        print(i)
        count += 1
    i += 1
print(f"Ther are {count} factors.")