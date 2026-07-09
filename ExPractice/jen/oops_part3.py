"""# Example
# Aggregation

class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)

   
class Address():
    def __init__(self,city,pin,state):
        self.__city = city
        self.pin = pin
        self.state = state
    
    def get_city(self):
        return self.__city
    
add1 = Address("Kathmandu",196001,"Kirtipur")
cust = Customer("Anuj","Male",add1)

cust.print_address()
"""




print(1+2)
print("1" + "2")