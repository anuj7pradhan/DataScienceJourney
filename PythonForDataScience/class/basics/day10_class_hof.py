# a = ["Pramila", "Ram", "Hari"]
# for i in a:
#     print(i)
# print()
# # High order function: 
#      #function inside function

# a = ["Pramila", "Ram", "Hari"]

# print(max(a,key=len)) # High order function

# Three Built-in high order function
# 1. map()
# 2. filter()
# 3. reduce()


# map():
        # map() python ko ek built-in higher order function jo jasle iterable
        # (list, tuple, set, ect.) ko pratek element ma euta function apply garera naya iterator object return garcha.

# def show(a):
#     return a + 2
# v = [1,2,3,4,5]
# print(show(v))


# def show(a):
#     return a + 2
# v = [1,2,3,4,5]
# result = map(show, v)
# print(list(result))



# Short way

# v = [1,2,3,4,5]
# result = map(lambda x: x ** 2, v)
# print(list(result))



# def show(a):
#     return a ** 2
# var = (1,2,3,45,23)
# result = map(show, var)
# print(tuple(result))



# def expo(a):
#     return a / 2
# div = {1,2,3,4}
# result = map(expo, div)
# print(list(result))



# v = [1,2,3,4,5]
# result = map(lambda x: x ** 2, v)
# print(list(result))

# Filter
# filter() le iterable bata condition milne element matra select garcha

# number = (1,2,3,4,88,6,7,89,12,1,223,11,23,43,234,56)
# def show(c):
#     return c%2==0
# var = filter(show, number)
# print(list(var))

# num1 = (1,2,3,4,88,6,7,89,12,1,223,11,23,43,234,56)
# result = filter(lambda x: x% 2 ==0,num1)
# print(list(result))

# odd = (1,2,3,4,88,6,7,89,12,1,223,11,23,43,234,56)
# result = filter(lambda x : x%2 != 0,  odd)
# print(list(result))

# var = {1,2,1,3,4,3,5}
# result = filter(lambda x : x+ 2 , var)
# print(set(result))

# upp = {"pramila","sharmila","ramila"}
# result = map(lambda x: x.upper(), upp)
# print(set(result))


# mark = [12,49,55,2,67]
# result = filter(lambda x : x >= 50,mark)
# print(list(result))

# text. which is > than 5,  print out

# new_str = {"pramila","hari","sharmila","ramila","sita"}
# result = list(filter(lambda x : len(x) > 5,  new_str))
# print(result)

# new_str1 = {"hari","hari","sumi","Aakash"}
# result = tuple(filter(lambda x : len(x) > 3, new_str1))
# print(result)

# reduce() function
# reduce: "reduce() le list ko sabai value jodera, multiply garera, ya combine garera euta matra output banaucha(merge)

# from functools import reduce

# from functools import reduce
# num = [1,2,3]
# def mul(x,y):
#     return x * y
# result = reduce(mul,num)
# print(result)

# from functools import reduce
# number = [1,2,3,4,5]
# result = reduce(lambda x,y : x + y, number)
# print(result)

from functools import reduce

# xyz = [1,2,3]
# result = reduce(lambda x,y: x * y, xyz)
# print(result)

a = ["Ram","Shyam","Hari","Gopal"]
b = reduce(lambda x,y: x+" "+ y,a)
print(b)