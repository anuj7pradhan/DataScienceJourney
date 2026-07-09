# # Loop:
# # If you are fixed then run for loop
# # If unsure then while loop

# # print("Hello")
# # print("Hello")
# # print("Hello")
# # print("Hello")
# # print("Hello")

# # Syntx
# # Basic syntax of for loop in python
# # for variable in sequence:
# #       Staterment

# # Using range()
# # for varialble in range(number)
# #       statement

# list1 = ["Pramila", "Shrestha"]
# for i in list1:
#     print(i)

# for i in range(5):
#     print("Hello")

# for i in range(5,10):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# for i in range(1,100):
#     if i % 2==0:
#         print(i)

# for i in range(1,21):
#     if i % 2 ==0:
#         print(i)

# for i in range (1,51):
#     if i % 2 != 0:
#         print(i) 

# 5 * 1 = 5


# num = int(input("Enter num: "))

# for i in range(1,11):
#     print(num,"*", i,"=",num * i)

# x = int(input("Enter sum num: "))
# total = 0
# for i in range(1,10):
#     total += i
# print(total)

# # for i in range (1,5):
# #     print("*")
# num = int(input("Enter num to fact: "))
# fact  = 1
# for i in range(1,num + 1):
#     fact *= i

# print(fact)

    

# Pattern: Numbers in triangle form

n = int(input("Enter n: "))
for i in range( 1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" ")

# 0 1 1 2 3 5 8 13

a= 0
b = 1
for k in range(10):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

