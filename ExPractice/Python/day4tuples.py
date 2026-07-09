# Tuples
# Introduction to tuples
# A collection of items which are indexed, ordered, and immutable

# Syntax:
#   tuple_name = (item1, item2, item3, ...)

cars = ('Audi', 'mercedez', 'bmw')
# index   0         1         2
print(cars)
# cannot be ubdate the tupple
# print(cars[0]) = 'Ferrari'

# Tuple with one item

car = ('Audi',)
print(car)

# Length of the tuple

cars = ('Audi', 'mercedez', 'bmw')
print(len(cars))

# tuple() constructor
cars = tuple(('Audi', 'mercedez', 'bmw'))
print(cars)