# Modules in Python
# Single python file

# Create a module mymodule.py file

# Use mymodule file

# import my_module
# my_module.say_hello("Anuj Pradhan")
# my_module.say_bye("Take good care")



# import / use specific part of code
from ExPractice.Module.my_module import person1
print(f"My age is ",person1,{"name"})

# Package: Collection modules/py files: + __init__ file

# Library: Collection of modules and packages
# Libraries in Python
    # Library is a collection. of modules and packages that provide pre-written functionality for your program.
    # Libraries are typically larger and more feature-rich than packages or modules.

# Why use libraries?
    # To avoid writing common functionality from scratch
    # To leverage powerful tools developed by the community

    # Ex.   # Pandas: for data manipulation
            # Matplotlib: for plotting and visualization.

# Using a library (Pandas)
import pandas as pd


# import math
# A = 36
# print(math.sqrt(A))

# from math import factorial
# B = 4
# print(B)