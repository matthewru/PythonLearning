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

    def is_on(self, pointOne, pointTwo):
        mOne = self.slope(pointOne)
        mTwo = self.slope(pointTwo)
        mThree = pointOne.slope(pointTwo)
        if mOne == 'undefined' and mTwo == 'undefined' and mThree == 'undefined':
            return True
        elif mOne == mTwo and mOne == mThree and mTwo == mThree:
            return True
        else:
            return False

# test cases
p = Point(0,2)
q = Point(4,2)
r = Point(1,0)
s = Point(8,2)
print(r.is_on(p, q))   # should be True
print(s.is_on(p,q))   # should be False