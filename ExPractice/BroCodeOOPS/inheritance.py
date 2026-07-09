# Inheritance -> Allows a class to inherit attributes and methods fro the another class
#             -> Helps with codde reusability and extensibility
#               -> class Child(Parent)

class Animal:                   # A parent class
    def __init__(self,name):
        self.name = name        # Attributes
        self.is_alive =  True   # Attributes

    def eat(self):              # Method "eat"
        print(f"{self.name} is eating.")

    def sleep(self):            # Method "sleep"
        print(f"{self.name} is sleeping.")

class Dog(Animal):              # A child class
#    pass


   """ 
    def __init__(self,name):
        self.name = name        # Attributes
        self.is_alive =  True   # Attributes

    def eat(self):              # Method "eat"
        print(f"{self.name} is eating.")

    def sleep(self):            # Method "sleep"
        print(f"{self.name} is sleeping.")
    
    """
   
   def speak(self):
       print("WOOF!")

class Cat(Animal):              # A child class
    # pass
    def speak(self):
        print("MEAU")

class Mouse(Animal):            # A child class
    # pass
    def speak(self):
        print("Squeez")

dog = Dog("Sheru")              # Making an object "dog"
cat = Cat("Mushu")              # Making an object "cat"
mouse = Mouse("Tichu")          # Making an object "mouse"


print(dog.name)                 # Calling attributes
print(dog.is_alive)             # Calling attributes
dog.eat()                       # A child class Calling methods "eat" from the parent class "Animal"
dog.sleep()                     # A child class Calling methods "sleep" from the parent class "Animal"
print()

print(cat.name)                 # Calling attributes
print(cat.is_alive)             # Calling attributes
cat.eat()                       # A child class Calling methods "eat" from the parent class "Animal"
cat.sleep()                     # A child class Calling methods "sleep" from the parent class "Animal"
print()

print(mouse.name)                 # Calling attributes
print(mouse.is_alive)             # Calling attributes
mouse.eat()                     # A child class Calling methods "eat" from the parent class "Animal"
mouse.sleep()                   # A child class Calling methods "sleep" from the parent class "Animal"

# Inheritance made a lot more easier
# If there were hundreds of classes then it will take a lots of time
# So here inheritance made easier write code once and reuse it.
# If i got to change any attributes , we will change only in one place

print()
dog.speak()
cat.speak()
mouse.speak()
