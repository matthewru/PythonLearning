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
