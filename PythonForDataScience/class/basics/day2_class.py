#String a collection of words, text, character, numbers, symbol

str1 = 'Hello, it\'s single quote'
str2 = "Hello, it\'s double quote"
str3 = '''Hello, it\'s triple quote'''

'''Hello, it\'s triple quote'''
print(str1,str2,str3)

# indexing

str = "learningpython"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[6])
print(str[-1])

#slicing
# Syntax =
    # string[start:end:step]
str_slice = "learningpythoninfotec"
print(str_slice[0:3])
print(str_slice[0:16])
print(str_slice[8:12])

print(str_slice[-1:-3])
print(str_slice[0:10:2])
#default
print(str_slice[::2])

print(str_slice[:-16:-1])
print(len(str_slice))

#text[:n] start to n -- last tirako character remove garne
str_last = "learningpythonIsBest"
print(str_last[:-4])
print(str_last[-6:])


print(str_last[10:])
print(str_last[:3])
print(str_last[::3])
print(str_last[::-3])
print(str_last[::-2])

user_in = input("Enter a word: ")
if user_in == user_in[::-1]:
    print(f"it's palandrome {user_in}")
else:
    print("if's not palandrome")


str1 = "learningpython"
print(str1.upper())
print(str1.capitalize())
print(str1.lower())
print(str1.count("s"))
print(str1.swapcase())
str4 = "learningpython"
print(str4.swapcase())


str5 = "       learningpython   "
print(str5.strip())
print(str5.rstrip())
print(str5.lstrip())
print("I am enjoying java".replace("java", "python"))


#ex

user_input = input("Enter a word: ")
print("Upper :",user_input.upper())
print("Lower :", user_input.lower())
print("Capitalizing: ", user_input.capitalize())
print("Replace: ", user_input.replace(user_input,"Hi, I just replaced you."))
print("Center: ",user_input.center(30))
