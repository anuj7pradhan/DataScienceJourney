"""Question

Create a Python program using Single Inheritance to manage a student's academic record.

Requirements
Create a parent class named Person.
Data members:
name
age
Create a constructor to initialize these values.
Create a method display_person() to display the person's details.
Create a child class named Student that inherits from Person.
Additional data members:
roll_no
faculty
Marks in:
Python
Java
DBMS
Networking
AI
Initialize all required data members.
Create the following methods:
calculate_total()
calculate_percentage()
calculate_grade()
Display:
Student Name
Age
Roll Number
Faculty
Marks of all subjects
Total Marks
Percentage
Grade
Create one object of the Student class and display the complete result.
"""


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Student Name: {self.name}\nAge: {self.age}")

class Student(Person):
    def __init__(self,name,age,roll_no, faculty,Python, Java, DBMS, Networking, AI):
        Person.__init__(self, name,age)
        self.roll_no = roll_no
        self.faculty = faculty
        self.Python = Python
        self.Java = Java
        self.DBMS = DBMS
        self.Networking = Networking
        self.AI = AI
   
    def calculate_total(self):
        return self.Python + self.Java + self.DBMS + self.Networking + self.AI

    def calculate_percentage(self):
        return (self.calculate_total() / 500) * 100
    
    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 91 and percentage <= 100:
            print("Grade A")
        elif percentage >= 81 and percentage <= 90:
            print("Grade B")
        elif percentage >= 71 and percentage <= 80:
            print("Grade C")
        elif percentage >= 61 and percentage <= 70:
            print("Grade C")
        elif percentage >= 51 and percentage <= 60:
            print("Grade D")
        elif percentage <= 41 and percentage > 0:
            print("Fail")
        else:
            print("Invalid Marks")

        # if percentage >= 90:
        #     return "A+"
        # elif percentage >= 80:
        #     return "A"
        # elif percentage >= 70:
        #     return "B+"
        # elif percentage >= 60:
        #     return "B"
        # elif percentage >= 50:
        #     return "C"
        # else:
        #     return "Fail"

    def Display(self):

        print("========Student Information=========")
        self.display_person()
        print(f"Roll No.: {self.roll_no}")
        print(f"Faculty: {self.faculty}")

        print("\nMarks of all subject")
        print(f"Python: {self.Python}")
        print(f"Java:{self.Java}")
        print(f"DBMS: {self.DBMS}")
        print(f"Networking: {self.Networking}")
        print(f"AI: {self.AI}") 

        print(f"\nTotal Marks: {self.calculate_total()}")

        print(f"Percentage: {self.calculate_percentage()}")
        self.calculate_grade()

st1 = Student("PRAMMILA",24,101,"PSM",79,88,67,78,99)
st1.Display()



