# Python Class 1889
# Lesson 3 Problem 5
# Author: madmathninja (272729)
class Jar:

    def __init__(self, liters, waterAmount = 0):
        self.liters = liters
        self.waterAmount = waterAmount

    def __str__(self):
        answer = ''
        answer += 'a '
        answer += str(self.liters)
        answer += ' liter jar with '
        answer += str(self.waterAmount)
        answer += ' liters of water'
        return answer
        #print("a %d liter jar with %d liters of water" % (self.liters, self.waterAmount))

    def fill_Jar(self):
        self.waterAmount = self.liters

    def empty_Jar(self):
        self.waterAmount = 0

    def pour_into_other_Jar(self, otherJar):
        while otherJar.waterAmount != otherJar.liters and self.waterAmount != 0:
            otherJar.waterAmount += 1
            self.waterAmount -= 1

#tests
threeLiter = Jar(3)
fiveLiter = Jar(5)
threeLiter.fill_Jar()
print(threeLiter)
print(fiveLiter)
threeLiter.pour_into_other_Jar(fiveLiter)
print(threeLiter)
print(fiveLiter)
threeLiter.fill_Jar()
print(threeLiter)
print(fiveLiter)
threeLiter.pour_into_other_Jar(fiveLiter)
print(threeLiter)
print(fiveLiter)
fiveLiter.empty_Jar()
print(threeLiter)
print(fiveLiter)
threeLiter.pour_into_other_Jar(fiveLiter)
print(threeLiter)
print(fiveLiter)
threeLiter.fill_Jar()
print(threeLiter)
print(fiveLiter)
threeLiter.pour_into_other_Jar(fiveLiter)
print(threeLiter)
print(fiveLiter)


