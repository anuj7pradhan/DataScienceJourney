# Q1. wap to check whether a person is eligible for voting or not.
# Accept age from user

age = int(input("Enter Your age:"))
if age >=18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")

# Q2. WAP to check whether a number entered by user is even or odd.

number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3. WAP to display "Hello" if a number entered by user is multiple of five.
# otherwise print "Bye"

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

    
# Q4. WAP to calculate the electricity bill 
# (accept number of unit from user) according to the followinng criteria:
#       Unit                    Price
#     First 100 units       no charge
#     Next 100 units        Rs. 5 per unit
#     After 200 units       Rs. 10 per unit
#     (For example if input unit is 350 than total bill amount is Rs.2000)

units = int(input("Enter units: "))
if units <= 100:
    print("No charge")
elif units > 100 and units <= 200:
    print(f"Rs. 5 per unit,i.e Rs.{(units - 100) * 5}")
elif units > 200:
    print(f"Rs. 10 per unit,i.e Rs.{500 + (units -200)* 10}")
else:
    print("Invalid units.")


# Q5.WAP to display the last digit of a number. 
#   (hint: any number % 10 will return the last digit) 

number = int(input("Enter a number: "))
print("Last digit of a number", number % 10)

# Q6. WAP to check whether the last digit of a number (Enntered by user) is divisible by 3 or not.

number = int(input("Enter number: "))
l_digit = number % 10
print("Last digit of a entered number is",l_digit)
if l_digit % 3 == 0:
    print(f"{l_digit} is divisible by 3.")
else:
    print(f"{l_digit} is not divisible by 3.")