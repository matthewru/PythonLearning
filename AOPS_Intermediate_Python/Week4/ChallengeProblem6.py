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
        self.simplify()
        return str(self.num) + '/' + str(self.denom)

    def getCommonFactor(self, number, otherNumber):
        common_factor = 1
        for i in range(min(abs(number), abs(otherNumber)), 1, -1):
            if number % i == 0 and otherNumber % i == 0:
                common_factor = i
                break
        return common_factor

    def simplify(self):
        common_factor = self.getCommonFactor(self.num, self.denom)
        while self.num % common_factor == 0 and self.num % common_factor == 0:
            self.num = int(self.num / common_factor)
            self.denom = int(self.denom / common_factor)
            if common_factor == 1:
                break
        if self.denom < 0:
            self.num = -self.num
            self.denom = abs(self.denom)
        elif self.denom < 0 and self.num < 0:
            self.num = abs(self.num)
            self.denom = abs(self.denom)
    # you should add more methods

    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.denom
        newOtherFractionNum = otherFraction.num * self.denom
        sum = Fraction(newNum + newOtherFractionNum, self.denom * otherFraction.denom)
        sum.simplify()
        return sum

    def __sub__(self, otherFraction):
        newNum = self.num * otherFraction.denom
        newOtherFractionNum = otherFraction.num * self.denom
        dif = Fraction(newNum - newOtherFractionNum, self.denom * otherFraction.denom)
        if dif.num == 0:
            dif.denom = 1
            return dif
        dif.simplify()
        return dif

    def __mul__(self, otherFraction):
        product = Fraction(self.num * otherFraction.num, self.denom * otherFraction.denom)
        product.simplify()
        return product

    def __truediv__(self, otherFraction):
        quot = Fraction(self.num * otherFraction.denom, self.denom * otherFraction.num)
        quot.simplify()
        return quot

    def __eq__(self, otherFraction):
        self.simplify()
        otherFraction.simplify()
        if self.num == otherFraction.num and self.denom == otherFraction.denom:
            return True
        else:
            return False

    def __float__(self):
        decimal = float(self.num/self.denom)
        return decimal


# examples
p = Fraction(3,6)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print -1/6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if overloading using special methods
print(p+q)  # should print 1/3
print(p-q)  # should print 2/3
print(p-p)  # should print 0/1
print(p*q)  # should print -1/12
print(p/q)  # should print -3/1
print(p==r) # should print True
print(p==q) # should print False