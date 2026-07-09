# # Session 4
#             # Loops

# # A Loop lets you run the same block of code multiple times 
# # without wiring it again and again.
# # Instead of doing this:

# print("Hello madam")
# print("Hello madam")
# print("Hello madam")
# print("Hello madam")
# print("Hello madam")
# print("Hello madam")
# print("Hello madam")
# print("Hello madam")
# print("Hello madam")
# print("Hello madam")


# i = 0
# while i < 10:
#     print("Hello Dear")
#     i += 1

# # Types of loops
#     # WHILE loop
#     # FOR loop

# # WHILE Loop

#     # A while loop keeps running as long as its condition is True.
#     # Python checks the condition before every iteration- the moment it becomes False, the loop stops.


# # Print Hello 10 times

# # while 9 > 3:
# #     print("Hello")
# #     print("Done")

# # Use Control C to stop the program

# i = 1
# while i <=10:
#     print("HELLO")
#     print("DONE")
#     i += 1
# print("Lost")


# 1 to n print, n is the number input by user.

# i = 1
# n = int(input("Enter n:"))
# while i <= n:
#     print(i, end=" ")
#     i += 1

# Start and end by user
# Start to end print using while loop


# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# i = start
# while i <= end:
#     print(i,end=" ")
#     i +=1
# print()
# print(f"After while loop, start value is {start}")



# Start to end print even numbers

# start = int(input("Enter number to start:"))
# end = int(input("Enter number to end:"))
# i = start
# while i <= end:
#     if i % 2 == 0:
#         print(i)
#     i += 1 
# print(f"Even numbers from {start} to {end}.")

# Start to end, numbers which are divisible from 3 and 4

# start = int(input("Enter number to start: "))
# end = int(input("Enter number to end: "))
# i = start
# while i <= end:
#     if i % 3 == 0 and i % 4 == 0:
#         print(i,end=" ")
#     i+=1


# end to start 10 to 1

# i = 10
# while i >= 1:
#     print(i, end=" ")
#     i-= 1

# end to start n to 
# start = int(input("Enter number start: "))
# end = int(input("Enter number end: "))

# i = end
# while i >=start:
#     print(i)
#     i-=1  