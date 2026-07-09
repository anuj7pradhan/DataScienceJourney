"""
# Encapsulation
    # Encapsulation is a fundamental principle in oop that focuses on bundling data
    # And the methods that operates on that data into a single unit called a class.
    # It allows you to control the access and visibility of the data and methods, 
    # providinng a way to protect and organize your code.

## Access MModifier ---> Encapsulation
"""

"""
## private ---> Accessible within a class
class Person:
    def __init__(self, name , age):
        ## Constructor
        self.__name = name  # __name means a Private variable
        self.__age = age    # __age means a Private variable

    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age}.")

person1 = Person("Sujan",23)
person1.display_info()
"""

"""
## Protected variable
class Person:
    def __init__(self,name,age):
        ## Constructor
        self._name = name  # _name means a Protected variable
        self._age = age    # _age means a Protected variable

    # def display_info(self):
    #     print(f"The person name is {self._name} and the age is {self._age}.")

# person1 = Person("Sujan",23)
# person1.display_info()


person2 = Person("Kripa",32)
dir(person2)
person2._age
"""


"""
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display_info(self):
        print(f"The person name is {self._name} and the age is {self._age}.")

student1 = Student("Bala",12)
student1.display_info()
"""

"""
## Public variable
class Person:
    def __init__(self,name,age):
        ## Constructor
        self.name = name  # _name means a Protected variable
        self.age = age    # _age means a Protected variable
     
    def display_info(self):
         print(f"This is {self.name} and I am {self.age}.")

p1 = Person("Padmakala",44)
p1.display_info()
"""