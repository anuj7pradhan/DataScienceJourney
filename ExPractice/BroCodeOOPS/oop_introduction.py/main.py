from car import Car
car1 = Car("Mustang", 2026, "Red", False)   # Creating Object
car2 = Car("BMW", 2026, "White", True)   # Creating Object
car2 = Car("Corvette", 2026, "Blue", True)   # Creating Object


# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# print()
# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)


car1.drive()
car1.stop()
car2.stop()

car1.describe()