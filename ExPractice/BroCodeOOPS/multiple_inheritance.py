# multiple inheritance ---> inherit from more than one parent class
#                        C(A,B)
# multilevel inheritance ---> inherit from a parent which inherits from another parent
#                   C(B) <- B(A) <- A
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
   
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
# rabbit.hunt() # AttributeError Rabbit object has no attribute 'hunt'
rabbit.eat()
rabbit.sleep()
print("***********")

hawk.hunt()
# hawk.flee()   #AttributeError: 'Hawk' object has no attribute 'flee'
hawk.eat()
hawk.sleep()
print("***********")

# Here the fish has both flee method and hunt methods so it has both attributes
fish.flee()
fish.hunt()
fish.eat()
fish.sleep()
