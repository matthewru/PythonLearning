#Class radio with a brand attribute
class Radio:
    def __init__ (self, strBrand = "Revo"):
        self.brand = strBrand
    
    def play(self):
        print("Playing song")

    def __str__(self):
        return self.brand

#Class car with a model and radio attributes
class Car:
    def __init__ (self, strModel = "None", rRadio = Radio()):
        self.model = strModel
        self.radio = rRadio

    def __str__(self):
        return "This is a %s car with a %s radio" % (self.model, self.radio)

#Create a car object
mustang = Car("Mustang", Radio("AZATOM"))

#Call the play method of the radio of the car
mustang.radio.play()

#Print the car
print(mustang)
