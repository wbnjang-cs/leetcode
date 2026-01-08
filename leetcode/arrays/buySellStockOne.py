def maxProfit(prices):
    mProfit = 0
    profit = 0 
    dailyDiff = 0

    for i in range(1, len(prices)):
        dailyDiff = prices[i] - prices[i-1]
        
        #dip detected, save current peak
        if dailyDiff < 0 and profit > mProfit:
            mProfit = profit
        
        profit += dailyDiff

        if profit < 0:
            profit = 0
    
    if profit > mProfit:
        mProfit = profit

    return mProfit

def maxProfitAnswer(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        #for each day, min price looks behind and sees what is the max profit I could have obtained
        #OR
        # for each day, look behind and see when I should have bought (what is smallest number I have seen)
        min_price = min(min_price, price)

        #see if max profit possible for each day is bigger than what I currently have
        max_profit = max(max_profit, price - min_price)

    return max_profit


def maxProfitResolve(prices):
    minP = float('inf')
    maxP = -1

    for price in prices:
        minP = min(price, minP)
        maxP = max(maxP, price-minP)
    
    return maxP



