import random

#Class Die randomly chooses an integer and gets the corresponding dice face from the map
class Die:
    faceMap = {1 :  ' ------\n|      |\n|  o   |\n|      |\n ------',
               2 :  ' ------\n| o    |\n|      |\n|    o |\n ------',
               3 :  ' ------\n| o    |\n|  o   |\n|    o |\n ------',
               4 :  ' ------\n| o  o |\n|      |\n| o  o |\n ------',
               5 :  ' ------\n| o  o |\n|  o   |\n| o  o |\n ------',
               6 :  ' ------\n| o  o |\n| o  o |\n| o  o |\n ------'}
    def __init__(self, intFaceValue = 1):
        self.faceValue = intFaceValue

    def spin(self):
        self.faceValue = random.randint(1,6)

    def __str__(self):
        return self.faceMap[self.faceValue]
