# Tuple = Ordered collection, Unchangable, Immutable, Repitition

tuple1 = (1, 2, 3, "anjal","learningpython")

print(type(tuple1))

# Indexing

print(tuple1[0:3:2])
print(tuple1[-3:-1])
print(tuple1[1:3])
print(tuple1[-4:-2])
print(tuple1[-1])

# Change tuple values with replacing a value
x = (1,2,3,4,"sis","hi")
y = list(x)
print(type(y))
y[3] = 33
x = tuple(y)
print(x)

print("Hello, let's change the value of the tuple")
original_tuple = (1,2,3,4,5,6,7,8,9)
Change_tuple = list(original_tuple)
Change_tuple[2] = 222
original_tuple = tuple(Change_tuple)
print(original_tuple)

# change the value by append

this_tuple = ("Apple", "Banana", "Cherry")
x = list(this_tuple)
print(type(x))

x.append("Mango")
print(x)


tuple3 = ("Apple", "Banana", "Cherry")
# Tuple predicts as a string
xyz = ("Orange",)


# tuple3 += xyz
# print(tuple3)

xyz += tuple3
print(xyz)

tuple4 = ("Apple", "Banana", "Cherry")
tuple5 = list(tuple4)
tuple5.pop(1)

#tuple5.remove("Apple")
print(tuple5)
tuple5.clear()
#del tuple5
print(tuple5)


# Tuple unpacking


student = ("Sangita", 23, "jadibuti")
Name, Age, Location =student
print(Name)
print(Age)

# tuple unpacking by using *

song = ("Meadeth", "sabin", "basan", "ap")
eng ,  nep , * c = song
print(eng)
print(nep)
print(c)

#Concatination of the tuple
x = (1,2,3,4,5)
y = (9,8,7,6,5)
z = x+y
print(z)

# Multiplication in tuple
x = (1,2,3,4,5)
y = x * 3
print(y)



# Dictionary

# ORdered = same orders
# changable
# DO not allow duplicates
# key : value
dict1 = {
    "name" : "sam",
    "age": 33,
    "location":"bhaktapur"
}
print(dict1)
print(len(dict1))

#Accessing data from dictionary


dict2 = {
    "brand" : "Ford",
    "model" : "mustang",
    "milage" : 88

}

print(dict2["model"])
print(dict2.get("model"))
print(dict2.keys())
print(dict2.values())
print(dict2.items())



# change item and values in dictionary
dict3 = {
    "brand" : "Ford",
    "model" : "mustang",
    "milage" : 88
}
# Update
print(dict3)
dict3["milage"] = 100
print(dict3)

dict3.update({"milage": 110})
print(dict3)

# Add dictionary items
dict3["color"] = "Red"
print(dict3)

dict3.update({"year" : 2025})
print(dict3)

# len_tuple = {"apple", "banana", "cherry"}
# print(f"this is the len of the given tuple: {len(len_tuple)}")

# print(len_tuple)

# # creating a tuple of 1 item
# one_tuple = ("one",)
# print(one_tuple)
# print(type(one_tuple))

