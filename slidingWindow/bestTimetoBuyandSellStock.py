def maxProfit(prices):
    maxProf = 0
    minSeen = prices[0]

    for day in prices:
        currProf = day - minSeen
        if currProf > maxProf:
            maxProf = currProf
        
        if day < minSeen:
            minSeen = day

    
    return maxProf

def maxProfitSliding(prices):
    l = 0
    r = 1
    maxProf = 0

    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
            r +=1
            continue

        currProf = prices[r] - prices[l]
        if currProf > maxProf:
            maxProf = currProf
        r +=1
    
    return maxProf


prices = [7,1,5,3,6,4]
print(maxProfitSliding(prices))