def moneyList(coinList, maxAmount):
    CoinNum = [0] #list of how many coins it takes to make the looped through amount

    for amount in range(1, maxAmount + 1): #loop through each amount 1 to maxAmount + 1
        leastCoins = maxAmount #worst case scenario
        for coin in coinList: #loop through all the coins in coinList
            if coin <= amount: #see which coins can help make up amount
                neededCoins = 1 + CoinNum[amount - coin] #to show how many coins are needed
                if neededCoins < leastCoins:
                    leastCoins = neededCoins #updates scenario
        CoinNum.append(leastCoins) #adds it to the list
    return CoinNum

def find_best_denomination(maxAmount):
    #maxAmount in case of worst case scenario
    bestAverage = maxAmount

    for coinOne in range(2, maxAmount): #looping through possible coinOnes and coinTwos for best combination
        for coinTwo in range(coinOne + 1, maxAmount + 1):
            coinList = [1, coinOne, coinTwo]
            newAverage = sum(moneyList(coinList, maxAmount)) / (maxAmount + 1)
            if newAverage < bestAverage:
                bestAverage = newAverage
                (bestcoinOne, bestcoinTwo) = (coinOne, coinTwo)
    return [1, bestcoinOne, bestcoinTwo]


print(find_best_denomination(99))