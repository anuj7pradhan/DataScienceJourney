# Q1. WAP to accept percentage from user and display the grade according to the follpwing criteria:
#       Marks           Grade
#       > 90                A
#       > 80 and <=90       B
#       >= 60 and <=80      C
#       below 60            D

# percentage = int(input("Enter percentage: "))
# if percentage > 90:
#     print("A")
# if percentage > 80 and percentage <= 90:
#     print("B")
# if percentage >=60 and percentage <= 80:
#     print("C")
# if percentage <60:
#     print("D")



# Q2. WAP to accept the cost price of a bike and 
# display the road tax to be paid according to the following crieteria:
#   Cost price (in Rs.)          Tax
#       > 100000                    15%
#       >50000 and <= 100000        10%
#       <= 50000                    5%

# tax = 0
# cp = int(input("Enter cost price: "))
# if cp > 100000:
#     print(cp + (15 /100 * cp))
# if cp  > 50000 and cp <= 100000:
#     print((10 / 100) * cp)
# else: 
#     tax = 5/100 * cp
#     print("Tax to be paid", tax)


# WAP to check whether an years is leap year or nnot.

# year = int(input("Enter a year: "))
# if year % 100 == 0:
#     if year % 400 == 0:
#         print("Leap year.")
#     else:
#         print("not a leap year.")
# else:
#     if year % 4 == 0:
#         print("Leap year.")
#     else:
#         print("Not a leap year.")




# WAP to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.

# num = int(input("Enter num to find day: "))
# if num == 1:
#     print("Sunday")
# elif num == 2:
#     print("Monday")
# elif num == 3:
#     print("Tuesday")
# elif num == 4:
#     print("Wednesday")
# elif num == 5:
#     print("Thursday")
# elif num == 6:
#     print("Friday")
# elif num == 7:
#     print("Saturday")
# else:
#     print("Enter num from 1 to 7")


# WAP to accept a number from 1 to 12 and 
# display name of the month and days in that month like 
# 1 for January and number of days 31 and so on.

# num = int(input("Enter num to find month: "))
# if num == 1:
#     print("January")
# elif num == 2:
#     print("February")
# elif num == 3:
#     print("March")
# elif num == 4:
#     print("April")
# elif num == 5:
#     print("May")
# elif num == 6:
#     print("June")
# elif num == 7:
#     print("July")
# elif num == 8:
#     print("August")
# elif num == 9:
#     print("September")
# elif num == 10:
#     print("October")
# elif num == 11:
#     print("November")
# elif num == 12:
#     print("December")
# else:
#     print("Enter num from 1 to 12")



# WAP to accept any city from the user and display monument of that city.

#       City           Monument
#   Kathmandu           Taleju
#   Pokhara             Fewa taal
#   Bhaktapur           nyatapol
#   lalitpur            krishna mandir

# city = input("Enter city:")
# if city.lower() == "kathmandu":
#     print("Taleju")
# elif city.lower() == "pokhara":
#     print("fewa taal")
# elif city.lower() == "Bhaktapur":
#     print("nyatapol")
# elif city.lower() == "lalitpur":
#     print("krishna mandir")
# else:
#     print("Select k , p, b, l")


    # https://csiplearninghub.com/python-if-else-conditional-statement-practice/#test2