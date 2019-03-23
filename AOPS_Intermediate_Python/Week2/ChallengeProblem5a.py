def getQuotientRemainder(number, divisor):
    returnList = []
    quotient  = int(number/divisor)
    remainder = number % divisor
    returnList.append(quotient)
    returnList.append(remainder)
    return returnList

def coinsCount(denomination, number):
    denomination.sort(reverse = True)
    coinCount = 0
    value = number
    for coinValue in denomination:
        results = getQuotientRemainder(value, coinValue)
        quotient = results[0]
        remainder = results[1]
        coinCount += quotient
        if remainder == 0:
            break
        elif remainder > 0:
            value = remainder

    return coinCount


def averageCoins(denomination):
    coinNumber = []
    for count in range(0, 100):
        coins = coinsCount(denomination, count)
        coinNumber.append(coins)
    averageCoinage = sum(coinNumber) / len(coinNumber)
    return averageCoinage



#getQuotientRemainder test cases
#print(getQuotientRemainder(7, 3))
#print(getQuotientRemainder(21, 2))

#coinsCount test cases
#print(coinsCount([1, 10, 25], 26))
#print(coinsCount([1, 10, 25], 87))

#averageCoins test case
print(averageCoins([1, 10, 25]))
#print(averageCoins([1, 5, 25]))
#print(averageCoins([1, 25, 50]))