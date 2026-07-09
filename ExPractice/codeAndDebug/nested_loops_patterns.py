# Nested loops

"""
while
while

for
for
"""

# for i in range(1,4):
#     print(f"i = {i}")
#     for j in range(10,14):
#         print(f"j = {j}")

"""
i = 1
j = 10
j = 11
j = 12
j = 13
i = 2
j = 10
j = 11
j = 12
j = 13
i = 3
j = 10
j = 11
j = 12
j = 13
"""

# Patterns

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()


"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

"""
*
* *
* * *
* * * *
* * * * *

"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# for i in range(1,6):
#     for j in range(1,i + 1):
#         print(j,end=" ")
#     print()


"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

# n = int(input("Enter num: "))
# for i in range(1,n + 1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

# n = int(input("Enter n: "))
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j, end=" ")
#     print()

"""
5 4 3 2 1 
4 3 2 1
3 2 1
2 1
1
"""
# for i in range(5, 0, -1): 
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()



"""
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
1 2 3 4 
1 2 3
1 2 
1
"""

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3 
5 4
5
"""

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()
# for i in range(2,5):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()


"""
         1
       1 2 3
     1 2 3 4 5
   1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8 9
   1 2 3 4 5 6 7
     1 2 3 4 5
       1 2 3
         1
"""
# First of all let's do
# Space pattern


# Ex. Space pattern 1
"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# Ex. Space pattern 2
"""
            5
          5 4
        5 4 3
      5 4 3 2
    5 4 3 2 1
"""
# for i in range(5,0,-1):
#     for k in range(1,i):
#         print(" ",end=" ")
#     for j in range(5,i - 1, -1):
#         print(j,end=" ")
#     print()


"""
         1
       1 2 3
     1 2 3 4 5
   1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8 9
   1 2 3 4 5 6 7
     1 2 3 4 5
       1 2 3
         1
"""

# for i in range(1,6):
#     for j in range(1,5 - i + 1):
#         print(" ",end=" ")
#     for k in range(1,(i * 2)-1 + 1):
#         print(k,end= " ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1,5 - i + 1):
#         print(" ",end=" ")
#     for k in range(1,(i * 2)-1 + 1):
#         print(k,end= " ")
#     print()



# for i in range(1,6):
#     for j in range(1,5 - i + 1):
#         print(" ",end=" ")
#     for k in range(1,(i * 2)-1 + 1):
#         print("*",end= " ")
#     print()
# for i in range(4,0,-1):
#     for j in range(1,5 - i + 1):
#         print(" ",end=" ")
#     for k in range(1,(i * 2)-1 + 1):
#         print("*",end= " ")
#     print()