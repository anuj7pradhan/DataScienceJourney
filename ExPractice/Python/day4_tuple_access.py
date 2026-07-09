# Accessing tuple items through positive indexing

# Each item of a tuple can be accessed through it's index.
# Syntax:
    # tuple_name[index]
cars = ('Audi', 'Mercedez', 'Bmw')
print(cars[1])

# Trying to access items out of the index range will result an IndexError
# Providing float or any other data types as index will result in TypeError

cars = ('Audi', 'mercedez', 'bmw')
print(cars[3])
print(cars[1.0])

"""
https://youtu.be/9nN-Pb6FHVs?list=PLBlnK6fEyqRhJ_qiFbz9KZB1CO1HXBDHb
"""