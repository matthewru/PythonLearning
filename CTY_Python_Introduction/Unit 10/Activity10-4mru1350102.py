class Flower:
    #Class variable flowerCount
    flowerCount = 0
    def __init__(self, objPetalcount, objSpecies):
        self.petals = objPetalcount
        self.species = objSpecies
        #using class variable by incrementing it by one
        #whenever a new object gets created.
        Flower.flowerCount += 1

    def bloom(self):
        print("My %s is blooming!" % self.species)

    def wither(self):
        print("All %d petals are falling off!" % self.petals)

#main program where we will use the Flower class
#Create several flower objects
flower1 = Flower(10, "daffodil")
flower2 = Flower(7, "anemone")
flower3 = Flower(15, "begonia")
flower4 = Flower(17, "irises")
flower5 = Flower(19, "aster")

#Print the class variable.
print("You've discovered %d different types of flowers!" % Flower.flowerCount)
