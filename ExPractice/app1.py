"""
def about_me(name, profession, pet):
    print("Hi my name is", name)
    print("I am a ",profession)
    print("My pet name is", pet)

about_me("Mariya", "programmer", "cat")
about_me("Gendalf", "wizard","eagle")
"""

import random
from sty import fg
def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg( red, green, blue)

red, green, blue = generateRGB()
colour = generateColour(red, green, blue)
print(colour,"I am randomly changing colour.")