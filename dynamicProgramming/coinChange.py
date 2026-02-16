def coinChange(coins, amount):
    if amount == 0:
        return 0

    d = {}
    coins.sort()
    for coin in coins:
        d[coin] = 1

    for i in range(amount+1):
        smallest = amount+1
        for coin in coins:
            if i - coin not in d:
                continue
            smallest = min(smallest, d[i-coin])

        if smallest == amount+1:
            continue
        d[i] = d.get(i, 1 + smallest)
    
    if amount not in d:
        return -1
    return d[amount]
    
def coinChangeAnswer(coins, amount):
    d = [amount + 1] * amount+1
    d[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin:
                d[i] = min(d[i], 1 + d[i-coin])
    
    return d[amount] if d[amount] != amount+1 else -1
