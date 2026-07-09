# # Exercise 1. Create a string made of the first, middle, and last character
# str1 = input("Enter a string: ")
# print(f"The first, middle, and last character of {str1} is:", str1[::2])

# # Exercise 2. Create a string made of the middle three characters

# str2 = input("Enter str2: ")
# middleIndex = int(len(str2) / 2)
# print(f"a string made of the middle three characters are:",str2[middleIndex - 1 : middleIndex +2])


# Exercise 3. Append new string in the middle of a given string
str3 = input("Enter str3: ")
str4 = input("Enter str4:")

# Middle index of first string
mid = int(len(str3) / 2)

# Get character from 0 to mid index
x = str3[:mid]

# Get character from mid index to end
y = str3[mid:]

# Combine and print all
print(f"This is append: {x + str4 + y}")



# Exercise 4. Create a new string made of the first, middle, and last characters of each input string

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

s1_first = s1[0]
s1_mid = s1[int(len(s1)/2)]
s1_last = s1[-1]



s2_first = s2[:1:]
s2_mid = s2[int(len(s2) / 2)]
s2_last = s2[-1]
print(s1_first,s2_first,s1_mid)

result = s1_first + s2_first + s1_mid + s2_mid + s1_last + s2_last

print(result)
