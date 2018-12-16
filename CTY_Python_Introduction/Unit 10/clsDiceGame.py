from clsDie import Die

#Class DiceGame has two dice objects 
class DiceGame:
    def __init__(self, dDieOne = Die(), dDieTwo = Die()):
        self.dieOne = dDieOne
        self.dieTwo = dDieTwo

    #When it rolls it calls the spin method from class Die for each die object.
    #It also displays the total face value and the face of each die after rolling.
    def roll(self):
        self.dieOne.spin()
        self.dieTwo.spin()
        print(self.dieOne)
        print(self.dieTwo)
        print("Face value: %d" % (self.dieOne.faceValue + self.dieTwo.faceValue))
