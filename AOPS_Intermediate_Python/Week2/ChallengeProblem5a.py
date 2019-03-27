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

coinList = [1, 10, 25]
moneyList = moneyList(coinList, 99)
print(sum(moneyList)/100) #averages it
