# Start to end print even numbers.

start = int(input("Enter start value: "))
end = int(input("Enter end value: "))
i = start

i=1
while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
