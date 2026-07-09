# List comprehension

    # Short and efficiency way to create new list using for loop and condition

# Syntax
#   [expression for item in iterable(list,set ,tuple)]

# With condition
    # [expression for item in iterable if condition]

# numbers = [1,2,3,4,5]
# new_list =[]

# for num in numbers:
#     new_list.append(num * 2)
# print(new_list)


# numbers = [1,2,3,4,5]
# result = [num * 2 for num in numbers]
# print(result)


result = [i for i in range(1,11)]
print(result)


sq = [i * i for i in range(1,5)]
print(sq)

cube = [ i ** i for i in range(1,5)]
print(cube)


                    # # List comprehension

#     # Short and efficiency way to create new list using for loop and condition

# # Syntax
# #   [expression for item in iterable(list,set ,tuple)]

# # With condition
#     # [expression for item in iterable if condition]
        # [expression if condition else expression for item in iterable]
# # numbers = [1,2,3,4,5]
# # new_list =[]

# # for num in numbers:
# #     new_list.append(num * 2)
# # print(new_list)


# # numbers = [1,2,3,4,5]
# # result = [num * 2 for num in numbers]
# # print(result)


# result = [i for i in range(1,11)]
# print(result)


# sq = [i * i for i in range(1,5)]
# print(sq)

# cube = [ i ** i for i in range(1,5)]
# print(cube)


# i = ["pramiLA","ruby","cuba"]
# up = [i.upper() for i in i]
# print(up)


# i = ["pramiLA","ruby","cubaa"]
# length = [len(i) for i in i]
# print(length)


# list1 = [1,2,3,4,5,6,7,8,9,10] 
# result = [x for x in list1 if x % 2 ==0]
# print(result)


# oddy = [1,2,3,4,5,6,7,8,9,10]

# result = [x for x in oddy if x % 2 != 0]
# print(result)

# sq = [1,2,3,4,5,6,7,8,9,10]
# result = [x * x for x in sq if x % 2 == 0] # Expression ma nai conditions dinu (x * x)
# print(result)

# list2 = [1,2,3,4,5,6,7,8,9,10]
# result = ["Even" if i %2==0 else "Odd" for i in list2]
# print(result)

# marks = {45,34,65,76,12,43,98}
# result = ["Pass" if i >=40 else "Fail" for i in marks]
# print(result)


# strings = {"dubdub","xyz","KIRTIKA"}
# result = [i.lower() if i == i.upper() else i.upper() for i in strings]
# print(result)

# numbers = [-1,-2,-3,-4,1,2,3,4]
# result = [0 if i <=0 else i for i in numbers]
# print(result)

