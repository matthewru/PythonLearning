# Python Class 1889
# Lesson 2 Problem 1
# Author: madmathninja (272729)
def gcd(a, b):
    '''finds the greatest common divisor of two given numbers
    using recursion'''
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a-b, b)
    else:
        return gcd(b-a, a)

#test case
print(gcd(11571, 1767))