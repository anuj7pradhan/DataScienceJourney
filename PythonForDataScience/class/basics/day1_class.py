# Variable
# it is a container to store data

a = 10
b = 13.3
 # pep 8 python enhancement 

for i in range(6):
    print(i)

# Different kind of CASE
# 1. snake case = data_science
# 2. Pascal case = DataScience used for making class
# 3. Camel case = dataScience 



_Total_Value = 100
total_value = 199
print(_Total_Value)
print(total_value)

#Data type
# Numeric datatype: int, float, complex
# text data : string
# boolean: True , false
# sequence data type: list, tuple, range
# mapped data type: dictionary
# Set
# byterray

comple = 10 + i

print(comple)

# list uses [] large bracet
# Mutable
# Ordered. collection
# changable
list = [1,3,'i',"a" , "Hello"]
print(list)


#Tuple uses small bracket ()
# Ordered collection
# Immutable
# unchagable

t1 = (1,"orange", "apple",2)

#Dictionary : key-value pairs, uses {} curley bracket
#mutable, ordered collection

dict  = {"Name":"Anuj",
         "Age": 23

         }
print(dict)
# set datatypes
# unordered collection, {}, index hunna
set = {True , 1,"Hi","asd","Hello", 1}
print (set)

#print formatting
# dot format: .format
# f-string
# % formating
name = "Ram"
age = 23
location = "bhaktapur"

# print as f-string
print(f"My name is {name}. I am {age} years old. I am from {location}.")
# print as
print("My name is",name,".I am ",age," years old. I am from",location)
 
#print as .format
print("My name is {}. I am {} years old. I am from {}.".format(name,age,location))

print("My name is %s. I am %d years old. I am from %s." %(name, age, location))

# input
name = input("Enter your name: ")
age = int(input("Enter your age:"))

a = input("Enter num 1:" )
b = input("Enter num 2:")

#print(a + b)
print(type(a))


#list ex

# fruits =["mango", "grapes","banana"]
# print(type(fruits))

# hobbies = ("singing", "Dancing", "Playing")
# print(hobbies)
# print(type(hobbies))

# name = input("Enter your name:" )
# age = int(input("Enter your age:"))
# print(f"My name is {name}.")
# print(f"My age is {age}.")

# print(type(name))
# print(type(age))

#Type casting : Manually

t1 = (1,2,3,4,5,54)
new_list = list(t1)
print(new_list)
print(type(new_list))

a = 23
b = str(a)
print(b)

# Data conversion
a = 12
b = 12.3
print(a+b)

#Operator

# addition


print(a + b) #add
print(a - b) #Sub
print(a * b) # Mul
print(a / b) # division
print( a ** b) #exponential
print(a // b) # Floor division
print(a % b) # modulus

# Assignment operators
# =, +=, -=, //=, %=
aa = 3
aa += 3
print(aa)