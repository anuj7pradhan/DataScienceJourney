# Manager
    # Waiter
    # Chef
    # Cleaner
"""
class Waiter:
    tables = []
Raj = Waiter()
Simran = Waiter()

Raj.tables = [4,5,6]
Simran.tables = [1,2]

print(Raj.tables)
print(Simran.tables)
print(Waiter.tables)
"""
# print("Hi")


class Waiter:
    def __init__(self):
        self.tables = []
    
    def take_order(self):
        print("Order taken")

    def add_table(self,table_number):
        self.tables.append(table_number)


Raj = Waiter()
Simran = Waiter()

Raj.tables.append(4)
Simran.tables.append(1)

Raj.take_order()
Simran.take_order()
Simran.add_table(1)



# print("Hi")





# https://youtu.be/OemVdsibSFQ


