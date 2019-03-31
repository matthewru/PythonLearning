# Python Class 1889
# Lesson 4 Problem 6
# Author: madmathninja (272729)

class Fraction:
    '''represents fractions'''

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError
        self.num = num
        self.denom = denom

    def __str__(self):
        pass

    # you should add more methods


# examples
p = Fraction(3,6)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print -1/6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if implementing "normal" arithmetic methods
print(p.add(q))       # should print 1/3, since 1/2 + (-1/6) = 1/3
print(p.sub(q))  # should print 2/3, since 1/2 - (-1/6) = 2/3
print(p.sub(p))  # should print 0/1, since p-p is 0
print(p.mul(q)) # should print -1/12
print(p.div(q))  # should print -3/1
print(p.eq(r))   # should print True
print(p.eq(q))   # should print False
### if overloading using special methods
print(p+q)  # should print 1/3
print(p-q)  # should print 2/3
print(p-p)  # should print 0/1
print(p*q)  # should print -1/12
print(p/q)  # should print -3/1
print(p==r) # should print True
print(p==q) # should print False