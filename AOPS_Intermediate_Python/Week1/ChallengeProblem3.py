def properDivisor(n):
    i = 1
    divisors = []
    while i<n:
        if n%i == 0:
            divisors.append(i)
        i = i + 1
    return divisors

def doubleperfectNumber():
    doubleperfects = []
    for number in range(100, 1000):
        if sum(properDivisor(number)) == 2 * number:
            doubleperfects.append(number)
    return doubleperfects

print(doubleperfectNumber())

