# For loop 1 to 10

# for i in range(1, 11):
#     print(i, end=" ")


# Steps in for loops

# for i in range(1,10,3): # here 3 is the step
#     print(i , end=" ")

# Negative for loop
    # 10 to 1
# for i in range(10,0,-1):
#     print(i, end = " ")

# Negative for loop even numbers from 10 to 1 

# for i in range(10,1,-1):
#     if i % 2 == 0:
#         print(i, end=" ")

# Dynamic for loop
# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
# for i in range(a,b):
#     print(i)

# BREAK Statement

    # break immediately stops the loop and exits it even if the condition is still True or there are items left in the sequence.

# CONTINUE Statement

    # continue skips the rest of the current iteration and jumps straight to the next one.
    # THe loop does not stop - it just skips that particular cycle.

 # 1 to 10
    # i = 5 loop stop


# i = 1
# while i <=10:
#     print(i,end=" ")
#     if i == 5:
#         break
#     i += 1

# i = 1
# while i <=10:
#     if i == 5:
#         break
#     print(i,end=" ")
#     i += 1

# i = 1
# while i <=10:
#     print(i,end=" ")
#     i += 1
#     if i == 5:
#         break

# Continue

# i = 0 
# while i <= 10:
#     i += 1
#     if 1 % 2 == 0:
#         continue
#     print(i,end=" ")

# Ex.   Take numbers as input from the user one by one. Skip negeative numbers and keep adding the positive ones.
        # Stop when the user enters 0 and print the. total. (Use both continue and break.)


# total = 0
# while True:
#     num = int(input("Enter num: "))
#     if num == 0:
#         break
#     if num < 0:
#         continue
#     total += num
# print(total)


# total = 0
# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
#     if num < 0:
#         continue
#     total += num
# print(total)

# for i in range(1,21):
#     if i % 2 ==0:
#         continue # Continue statement just continue to print another 
#     print(i,end=" ")






