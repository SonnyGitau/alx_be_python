class Dog:
    def __init__(self,name,breed,age) :
        self.name = name
        self.breed = breed
        self.age = age
    def bark(self):
        return "Woof! Woof!"
#object creation 
Dog1 = Dog("Robin", "Japanesse Spitz", 3)
Dog2 = Dog("Dots", "Dalmatian ", 5)

#Accessing object properties and methods .
print(f"{Dog1.name} is a {Dog1.breed} aged {Dog1.age} months. He says {Dog1.bark()}") 
print(f"{Dog2.name} is a {Dog2.breed} aged {Dog2.age} months. He says {Dog2.bark()}") 

class Animal :
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sounds(self):
        pass

#Inheritance
class Cat(Animal):
    def sounds(self):
        return f"{self.name} meows softly!"
class Elephant(Animal):
    def sounds(self):
        return f"{self.name} trumpets loudly!"
#polymorphism
zoo = [
    Cat("Whiskers", "Cat"),
    Elephant("Dumbo", "Elephant"),
]
for animal in zoo:
    print(animal.sounds())