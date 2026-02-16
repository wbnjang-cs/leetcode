def minCostClimbingStairs(cost):

    if len(cost) <= 2:
        return min(cost[0], cost[1])

    minCost = 0
    stairDict = {0: cost[0], 1: cost[1]}
    for stair in range(2, len(cost)):
        stairDict[stair] = min(cost[stair] + stairDict[stair-1], cost[stair] + stairDict[stair-2])
    
    return min(stairDict[len(cost)-1], stairDict[len(cost)-2])



def MinCostClimbingStairsCompact(cost):
    if len(cost) == 0:
        return
    elif len(cost) == 1:
        return cost[0]
    elif len(cost) == 2:
        return min(cost[0], cost[1])
    
    first = cost[0]
    second = cost[1]
    current = 0
    for stair in range(2, len(cost)):
        current = cost[stair] + min(first, second)
        first = second
        second = current
    
    print(f"second is {second}, current is {current}")
        
    
    return min(first, second)

        


cost = [1,100,1,1,1,100,1,1,100,1]
print(MinCostClimbingStairsCompact(cost))

cost2 = [10,15,20]
print(MinCostClimbingStairsCompact(cost2))
