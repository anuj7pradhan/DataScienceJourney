# File Handling:
# File Handling is the process of creating, reading, writing, updating and deleting files using the program.
# It allows us to store data permanently.


# A file is a collection of data stored permanently on a storage device
    # Ex.
    #   student.txt
    #   marks.txt
    #   notes.txt

# 4. Types of files
# 1. text file: a file is a text file that contains only text format
    # student.txt
    # notes.txt
    # data.csv

# 2. Binary file: a file is a binary file that contains only binary forma
    # image.img
    # video.mp4
    # music.mp3
    # document.pdf

# Process of handling files
    # 1. open file
    # 2. perform operation (Read, write)
    # 3. close file

# syntax
    # file = open("filename","mode")

# open: function of opening file
# mode: purpose of opening file

# ----> x : create a file
# f = open("msg.txt","x")

# ----> r : read a file

# f = open("msg.txt", "r")
# # print(f.readline())
# print(f.readlines())

# ----> w : write a file

f = open("msg.txt", "w")
f.write("learningpython")

# -----> a: Append to a file

f = open("msg.txt", "a")
f.write("\nbalkumari")

# -----> r+: write and read a file

f = open("msg.txt","r+")
f.write("\nTinkune")
print(f.read(2))

# What happens when we don't close the file?
# data will be corrupt
# data may not saved properly
# Memory and system resources ramain occupied
# It can cause resource leaks

try:
    f = open("msg.txt", "w")
    # print(f.read(2))

finally:
    print(f.close())

with open("msg.txt", "w") as f:
    f.write("Hi")
    print(f.readlines)
print(f.closed)

f = open("msg.txt", "w")
f.write("Hello dear how are you?")


# tell()
f = open("msg.txt", "r")
print(f.read(3))
print(f.tell())
# seek()
f.seek(0)
print(f.read(5))


# delete file
import os
os.remove("msg.txt")