# Polymorphism


# --> Polymorphism: One method, Many forms
# --> Occurance of sometimes in multiple forms

# Types 
#   1. Compile time polymorphism
    #   --> method overloading

#   2. Run time polymorphism
    #   --> method overriding


#   1. Compile time polymorphism
    # class contain more then one method with same name but different parameter


# class A:
#     def show(self):
#         print("No arguments")
    
#     def show(self,a,b):
#         print(a+b)

#     def show(self, a,b,c):
#         print(a+b+c)

# ob1 = A()
# ob1.show()
# ob1.show(1,2)
# ob1.show(1,2,3)

# Solution

# class A:
#     def show(self,a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             s = a + b + c
#         elif a != None and b != None and c == None:
#             s = a + b
#         elif a == None and b == None and c == None:
#             s = "No Arguments passed"
#         print(s)

# ob = A()
# ob.show()
# ob.show(1,2)
# ob.show(1,2,3)


"""
Question

Create a class named Electricity.

Create a method named bill() using default arguments (None) that performs 
the following tasks:

If no arguments are provided, print "No Data Found".
If only Units are provided, calculate the bill at Rs. 12 per unit.

If Units and Rate are provided, calculate the bill using the formula:
Bill = Units × Rate

If Units, Rate, and Tax (%) are provided, calculate the Final Bill by adding the tax 
to the total bill.

"""

class Electricity:
    def bill(self,units = None, rate = None, tax = None):
        if units == None and rate == None and tax == None:
            print("\nNo Data Found")
        
        elif units != None and rate == None and tax == None:
            total_bill = units * 12
            print(f"\nUnits: {units}")
            print(f"Total bill: {total_bill}")
        
        elif units != None and rate != None and tax == None:
            total_bill = units * rate
            print(f"\nUnits: {units}")
            print(f"Rate: {rate}")
            print(f"Total Bill: {total_bill}")


        elif units != None and rate != None and tax != None:
            total_bill = units * rate
            final_bill = total_bill + (total_bill * tax / 100)

            print(f"\nUnits: {units}")
            print(f"Rate: {rate}")
            print(f"Tax: {tax}")
            print(f"Total Bill: {total_bill} ")
            print(f"Final Bill: {final_bill}")


ob = Electricity()
ob.bill()
ob.bill(7)
ob.bill(2,12)
ob.bill(3,12,13)