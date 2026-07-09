# Adding elements to a list

# Elements can be added to alist in differnt ways, follwing are the methods to add elements to a list.

"""
1. append()
2. insert()
3. extend()
"""



# 1. append() method 
# A built-in method used to add an item at the end of a list.
# Syntax: 
#   list.appennd(value)

languages = ['c','cpp', 'java']
print(languages)

# append() 
languages.append('python')
print(languages)

# duplicate append() method to add multiple items
languages.append('ruby')
languages.append('javascript')
languages.append('php')

print(languages)

# A list as an item can be added.
languages.append(['ruby','js'])
print(languages)


# Insert method:  insert()
# A built-in method used to add an item at a specific positon
# Syntax:
#    list.insert(position, value)
artist = ['megadeth', 'metallica', 'korn', 'scorpion']
artist.insert(1, 'sabinRai')
print(artist)

num = [1,2,4,5]
num.insert(2,3)
print(num)

# Extend method : extend()
# A built-in method used to add all the items of onne list in aother list

# syntax:
#   list1.extend(list2)

lang = ['c','cpp','java']
more_lang = ['python', 'dart','ruby']
lang.extend(more_lang)
print(lang)