def climbStairs(n):
    stepNums = {0: 0, 1:1, 2:2}
    def countSteps(m):
        if m in stepNums:
            return
        else:
            stepNums[m] = stepNums[m-1] + stepNums[m-2]
    
    for i in range(n+1):
        countSteps(i)
        
    
    return stepNums[n]


def climbStairsBetter(n):
    stepNums = {0: 1, 1:1}
    for i in range(2, n+1):
        stepNums[i] = stepNums[i-1] + stepNums[i-2]
        
    print(stepNums)
    return stepNums[n]
print(climbStairsBetter(4))

        
        