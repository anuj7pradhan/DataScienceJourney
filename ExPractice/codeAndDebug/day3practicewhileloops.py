# Q1. 1 to 10 print

i = 1
while i<=10:
    print(i)
    i += 1


# Q2. 1 to n print, n is the number input by user
n = int(input("Enter your number: "))
i = 1
while i <= n:
    print(i)
    i += 1

# start and end by user
# start to end print using while loop

start = int(input("Enter start:"))
end = int(input("Enter end:"))


while start <= end:
    print(start)
    start += 1
print(f"After while loop, start value is {start}")


start = int(input("Enter start:"))
end = int(input("Enter end:"))
i = start

while i <= end:
    print(i, end=",")
    i += 1
print(f"After while loop, start value is {start}")
