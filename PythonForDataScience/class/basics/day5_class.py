# Dictionary

# ORdered = same orders
# changable
# DO not allow duplicates
# key : value


'''
dict1 = {
    "key" : "value"
'''

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


# Remove the value from the dictionary: pop(), popitem(), del, clear()
song = {
    "sabin" : "guras",
    "nabin": "sathi",
    "john" : "gravity"
}

print(song)

# pop()
# specify the keyword
song.pop("nabin")

# popitem
# removes the last item from the dictionary
song.popitem()
print(song)


student = {
    "name" : "sam",
    "age": 33,
    "location":"bhaktapur",
    "language": "python"
}
# del using key word
del student["language"]
print(student)
# del student
# print(student)

student.clear()
print(student)


student1 = {
    "name" : "sanjog",
    "age": 33,
    "location":"bhaktapur",
    "language": "python"
}
print(student1)
# copy

new_student = student1.copy()
print(f"This is new student: {new_student}")

for i in student1:
    print(i)

# Nested dictionary

student_1={
    "student1":{
        "name" : "Pratik",
        "marks" : 89,
        "age" : 23
    },
    "student2":{
        "name" : "sanumaya",
        "marks" : 67,
        "age" : 22,
        "location": "kirtipur"
    },
    "student3":{
        "name":"Mahesh",
        "marks": 66,
        "age": 23,
        "location":"sanothimi"
    }
}
print(student_1)