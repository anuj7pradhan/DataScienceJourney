'''
Q1:  Take two numbers as input from the user. Print their sum, difference, product, and remainnder.
'''

# num1 = int(input("Enter num 1 = "))
# num2 = int(input("Enter num 2 = "))
# print(f"Sum = {num1 + num2}")
# print(f"Difference = {num1 - num2}")
# print(f"Product = {num1 * num2}")
# print(f"Remainder = {num1 % num2}")



'''
Q2: Take a number as input. Print whether it is even or odd using the % operator and a comparision operator.
'''
# num1 = int(input("Enter num 1 = "))

# print(num1 % 2 == 0)


'''
Q3: Take the user's age as input. Check and print whether they are eligible to vote (age>= 18) and whether they are a senior citizen (age >= 60).
print both results.
'''

age = int(input("Enter age = "))
can_vote = age >= 18
senior_citizen = age >= 60
print(f"User can vote: {can_vote}")
print(f"User is sinior citizen: {senior_citizen}")


'''
Q4:  A student scored marks in 3 subjects. Take all three as input, calculate the total and average, and print both using an f-string.
'''

sub1 = int(input("Enter marks in sub1 = "))
sub2 = int(input("Enter marks in sub2 = "))
sub3 = int(input("Enter marks in sub3 = "))

total = sub1 + sub2 + sub3
average = total / 3
print(f"The total marks scored = {total} marks and the average is {average:.2f}")