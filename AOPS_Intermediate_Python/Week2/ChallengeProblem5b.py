def moneyList(coinList, maxAmount):
    CoinNum = [0]

    for amount in range(1, maxAmount + 1):
        leastCoins = maxAmount
        for coin in coinList:
            if coin <= amount:
                neededCoins = 1 + CoinNum[amount - coin]
                if neededCoins < leastCoins:
                    leastCoins = neededCoins
        CoinNum.append(leastCoins)
    return CoinNum

coinList = [1, 10, 25]
moneyList = moneyList(coinList, 99)
print(sum(moneyList)/100)







from itertools import combinations

def coinsCount(value, coins):
    if value <= 0:
        return 0 #We can only make change for positive values!
    else:
        #one option is to just use pennies
        smallestChange = value
        #but we should think about using other coins if they will fit
        for coin in coins:
            if coin <= value:
                #consider making change with one of this coin, and however many other coins we need
                numCoins = 1 + coinsCount(value - coin, coins)
                if numCoins < smallestChange:
                    smallestChange = numCoins #we found a better option!
    return smallestChange # return the best option

def averageCoins(coins):
    coinNumber = []
    for i in range(0, 100):
        print(i)
        numCoins = coinsCount(i, coins)
        coinNumber.append(numCoins)
        print(coinNumber)
    averageCoinage = sum(coinNumber) / len(coinNumber)
    return averageCoinage

def twoNumberCombo():
    numbers = range(2, 100)
    items = list(combinations(numbers,2))
    return items

def betterCoinage():
    combos = twoNumberCombo()
    bestAverage = 100
    for combo in combos:
        print("combo: %s" % str(combo))
        print("best average: %s" % str(bestAverage))
        average = averageCoins([1] + list(combo))
        if average < bestAverage:
            bestAverage = average
    return bestAverage


#print(averageCoins([1, 10, 25]))
print(betterCoinage())