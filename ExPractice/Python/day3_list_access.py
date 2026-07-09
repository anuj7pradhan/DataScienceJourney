# Topic
# Accessing elements of a single-dimentional list
# Negative indexing
# Accessing elements of a multidimentional list

# A single-dimentional list is a list where elements are listed one after the other
# Each element is allowed a unique number called index.

# Ex
# a list containing multiples of 5 upto 20

my_list = [5,10,15,20]
#index     0  1  2  3 
# access 1st element
print(my_list[0])
# access 4th element
print(my_list[3])

# Negative Indexing
# Accessing elements from the last
# ex:
neg_list = [5,10,15,20]
#index     -4 -3 -2 -1
print(neg_list[-1])
print(neg_list[-3])

#Accessing elements of a multi-dimentional list
# multidimentional list is a list containing another list

#eg 
mul_list = [[1,2,3], "Neo", [4,5,6], 3]
#index         0       1        2    3 
print(mul_list[0])
# Access list of a list
print(mul_list[0][1])

print(mul_list[2])
print(mul_list[2][1])

# Homework Practice
my_list3 = [[1,2,3],[['a','b','c'],5,6]]

# How to access the value 'b' in the above list?

print(my_list3[1][0][1])