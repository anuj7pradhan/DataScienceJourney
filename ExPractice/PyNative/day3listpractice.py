#list = ["surya","shakti","hima","sima","roma","jack"]
"""
Write a script to perform the following three operations on given list

Access the third element of a list
List Length: Print the total number of items
Check if the list is empty 

Given Input: numbers = [10, 20, 30, 40, 50]

1. Third element: 30
2. Length of list: 5
3. Is the list empty? False
"""

# Given
numbers = [10,20,30,40,50]

# Ler's print the third element of the items
print(f"Third element: {numbers[2]}")

#find the length of the list
print(f"Length of the list:",len(numbers))

# Find whether the given list is emmpty or not
print(f"Is the list empty? {len(numbers) ==0}")

"""
Exercise 2. Perform List Manipulation
Practice Problem: Take a given list and modify it through five specific actions:

1. Change Element: Change the second element of a list to 200 and print the updated list.
2. Append Element: Add 600 o the end of a list and print the new list.
3. Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
4. Remove Element (by value): Remove 600 from the list and print the list.
5. Remove Element (by index): Remove the element at index 0 from the list print the list.
6. Exercise Purpose: Python lists are mutable, meaning they can be changed after they are created. This exercise demonstrates the various ways to “reshape” your data dynamically during execution.

Given Input: Initial List: [100, 50, 400, 500]
"""
initial_List = [100, 50, 400, 500]
print(initial_List)
# 1. Change Element: Change the second element of a list to 200 and print the updated list.

initial_List[1] = 200
print(f"Updated list is {initial_List}")


# 2. Append Element: Add 600 to the end of a list and print the new list.

initial_List.append(600)
print(f"Add 600 to the end: {initial_List}")


# 3. Insert Element: Insert 300 at the third position (index 2) of a list and print the result.

initial_List.insert(2,300)
print(f"Insert 300 at third position: {initial_List}")


# 4. Remove Element (by value): Remove 600 from the list and print the list.

initial_List.remove(600)
print(f"Remove 600 from the list by value: {initial_List}")


# 5. Remove Element (by index): Remove the element at index 0 from the list print the list.

initial_List.pop(0)
print(f"Remove the element atf index 0: {initial_List}")

"""
Exercise 3. Sum and Average of All Numbers in a List
Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).

Exercise Purpose: Aggregation is the heart of data science. This exercise teaches you how to reduce a collection of multiple data points into a single, meaningful summary statistic.


"""

list3 = [10,20,30,40,50]
print(list3)

print(f"The sum of the given list: {sum(list3)}")
print(f"The average of the given list: {sum(list3) / len(list3)}")

"""
Exercise 4. Find Maximum and Minimum from List
Practice Problem: Identify the largest and smallest numerical values within a provided list.

Exercise Purpose: Finding extremes is vital for tasks like identifying the “best” price, the “highest” score, or detecting “outlier” data points in a dataset.

Given Input: Data: [45, 12, 89, 2, 67]
"""

data = [45, 12,89, 2, 67]
print(data)
print(f"The maximum from the given list is: {max(data)}")
print(f"The minimum from the given list is: {min(data)}")


"""
Exercise 5. Calculate the Product of All Elements
Practice Problem: Multiply every number in a list together to find the total product.


Exercise Purpose: While sum is built-in, “product” often requires you to think about how to accumulate values. This exercise reinforces the concept of an “accumulator variable” in a loop.

Given Input: Factors: [2, 3, 5, 7]

Expected Output: Product: 210
"""

factors = [2,3,5,7]
print(factors)
print(f"The multiplication of the given list is:{factors}")


"""
Exercise 6. Count Even and Odd Numbers
Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

Exercise Purpose: This introduces Flow Control and the Modulo Operator. It is a classic “Filtering” pattern where you categorize data based on a mathematical property. In real-world apps, this is the foundation for things like alternating row colors in a table or batching jobs into two different queues.

Given Input: Numbers: [10, 21, 4, 45, 66, 93, 11]
"""

numbers= [10, 21, 4, 45, 66, 93, 11]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")


"""
Practice Problem: Take a list and reverse the order of its elements.

Exercise Purpose: Reversal is a fundamental operation in data structures (like reversing a string or a linked list). Python provides multiple ways to do this, and understanding the difference between In-place Reversal (changing the original) and Slicing (creating a new one) is crucial for memory management.

Given Input: List: [100, 200, 300, 400, 500]

Expected Output: Reversed List: [500, 400, 300, 200, 100]
"""


list= [100, 200, 300, 400, 500]
reversed_list = list[::-1]
print(f"Reversed list: {reversed_list}")


"""
Exercise 8. Sort a List of Numbers
Practice Problem: Sort a list of numbers in ascending order (lowest to highest).

Exercise Purpose: Sorting is perhaps the most studied topic in Computer Science. It turns chaotic data into organized data, which is a prerequisite for high-speed search algorithms like Binary Search. Python uses Timsort, an efficient, hybrid sorting algorithm.

Given Input: Unsorted: [56, 12, 89, 3, 22]

Expected Output: Sorted List: [3, 12, 22, 56, 89] 
"""

unsorted = [56, 12, 89, 3, 22]
unsorted.sort()
print(f"Sorted list: {unsorted}")


"""
Exercise 9. Create a Copy of a List
Practice Problem: Create a copy of an existing list so that modifying the copy does not change the original.


Exercise Purpose: This exercise addresses one of the most common “gotchas” for new Python programmers: Pass-by-Object-Reference. If you simply write list_b = list_a, both variables point to the same list in memory. Learning to “Clone” or “Copy” is vital for data integrity.

Given Input: Original: ["Apple", "Banana", "Cherry"]


"""


original= ["Apple", "Banana", "Cherry"]
copy = original.copy()
print(copy)



"""
Exercise 10. Combine Two Lists
Practice Problem: Merge two separate lists into a single, unified list.

Exercise Purpose: Data often arrives in fragments from different sources (e.g., two different database queries). Combining or “Concatenating” them is the first step in data aggregation.

Given Input:

List A: ["Physics", "Chemistry"]
List B: ["Maths", "Biology"]
Expected Output: Combined List: ['Physics', 'Chemistry', 'Maths', 'Biology']
"""
list_a = ["Physics", "Chemistry"]
list_b = ["Maths", "Biology"]

print(f"List a: {list_a}")
print(f"List b: {list_b}")

list_a.extend(list_b)
print(f"List a cmbined to list b: {list_a}")


"""
Exercise 11. List Slicing: Extract Middle Elements

Practice Problem: Given a list, extract a “slice” containing the middle three elements.

Exercise Purpose: Slicing is one of Python’s most powerful features. Unlike many languages that require manual loops to copy array sub-sections, Python uses [start:stop] syntax. This forms the foundation for data windowing and pagination in web development.

Given Input: List: [10, 20, 30, 40, 50, 60, 70]

Expected Output: Middle Three: [30, 40, 50]

"""

original_list = [10, 20, 30, 40, 50, 60, 70]

middle_three = original_list[2:5]
print(f"Original list: {original_list}")
print(f"Middle three slicing: {middle_three}")


"""
Exercise 12. Swap Two Elements at Given Indices
Practice Problem: Write a script to swap the positions of two elements in a list based on their indices.

Exercise Purpose: Swapping is the heart of every sorting algorithm like Bubble Sort or Quick Sort. While other languages require a temporary variable to hold a value during the swap, Python offers an elegant, one-line tuple unpacking method that is faster to write and less error-prone.

Given Input:

List: [23, 65, 19, 90]
Indices to Swap: 0 and 2
"""
list = [23, 65, 19, 90]
index1 = 0
index2 = 2

print(list)
list[index1],list[index2] = list[index2], list[index1]
print(list)

"""
Exercise 13. Access Nested Lists (Simple Indexing)
Practice Problem: Given a “list of lists,” access a specific item hidden inside the inner list.

Exercise Purpose: This exercise teaches you to navigate Multi-dimensional Data. Think of nested lists like a spreadsheet (Rows and Columns) or a theater seating chart. To find a specific seat, you need the row and seat numbers.

Given Input:

Nested List: [[1, 2], [3, 4, 5], [6, 7]]
Goal: Access the number 5.
Expected Output: Accessed Value: 5
"""

nested_ist = [[1, 2], [3, 4, 5], [6, 7]]
access_num = nested_ist[1][2]
print(f"Nested list: {nested_ist}")
print(f"Access the number 5: {access_num}")


"""
Exercise 14. Check if List Contains a Specific Item
Practice Problem: Write a check to see if a certain value exists within a list and print a message based on the result.

Exercise Purpose: This is a Membership Test. It’s the logic used for “Is this username taken?” or “Is this item in the shopping cart?” Python’s in operator makes this incredibly readable, almost like plain English.

Given Input:

Inventory: ["Laptop", "Mouse", "Monitor", "Keyboard"]
Target: "Tablet"

Expected Output: Is Tablet in inventory? False
"""

inventory= ["Laptop", "Mouse", "Monitor", "Keyboard"]
target= "Tablet"

print(f"Inventory{inventory}")
if target in inventory:
    print(f"Is {target} in inventory? True")
else:
    print(f"Is {target} in inventory? False")

"""

"""


words= ["PHP", "Exercises", "Backend", "Python"]

longest = max(words, key=len)
print(longest)







