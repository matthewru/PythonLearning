#Define the class
class Flower:
    def __init__(self, objPetalcount, objSpecies):
        self.petals = objPetalcount
        self.species = objSpecies

    def bloom(self):
        print("My %s is blooming!" % self.species)

    def wither(self):
        print("All %d petals are falling off!" % self.petals)

    def __str__(self):
        return "A" + " " + self.petals + " " + "petaled" + " " + self.species + "!"

#main program where we will use the Cake class
newFlower = Flower("5", "tulip")

#Print the newFlower
print(newFlower)
