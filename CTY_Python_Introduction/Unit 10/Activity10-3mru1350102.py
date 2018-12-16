#Define the classes
class Flower:
    def __init__(self, objPetalcount, objSpecies):
        self.petals = objPetalcount
        self.species = objSpecies

    def bloom(self):
        print("My %s is blooming!" % self.species)

    def wither(self):
        print("All %d petals are falling off!" % self.petals)

class Pencil:
    def __init__(self, objSharpness, objColor):
        self.sharpness = objSharpness
        self.color = objColor

    def write(self):
        print("I'm writing with my %s pencil!" % self.sharpness)

    def erase(self):
        print("Erasing with my %s pencil!" % self.color)

#Creating two objects for each class
daisyFlower = Flower(42, "daisy")
daisyFlower.bloom()
daisyFlower.wither()
print(daisyFlower.petals)
print(daisyFlower.species)
              
tulipFlower = Flower(6, "tulip")
tulipFlower.bloom()
tulipFlower.wither()
print(tulipFlower.petals)
print(tulipFlower.species)


mechanicalPencil = Pencil("sharp", "black")
mechanicalPencil.write()
mechanicalPencil.erase()
print(mechanicalPencil.sharpness)
print(mechanicalPencil.color)
              
numbertwoPencil = Pencil("dull", "yellow")
numbertwoPencil.write()
numbertwoPencil.erase()
print(numbertwoPencil.sharpness)
print(numbertwoPencil.color)
