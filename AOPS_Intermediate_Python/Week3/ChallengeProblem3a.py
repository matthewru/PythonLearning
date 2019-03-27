# Python Class 1889
# Lesson 3 Problem 3 Part (a)
# Author: madmathninja (272729)

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def slope(self, pointTwo):
        if pointTwo.x == self.x:
            return "undefined"
        else:
            return (pointTwo.y - self.y) / (pointTwo.x - self.x)

# test cases
p = Point(1,-2)
q = Point(3,5)
r = Point(3,7)
print(p.slope(q))  # should be 3.5
print(q.slope(p))  # should be 3.5
print(q.slope(r))  # should print "undefined"