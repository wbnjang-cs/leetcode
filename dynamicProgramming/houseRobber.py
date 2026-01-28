def rob (nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    maxIncome = 0

    maxDict = {0 : nums[0], 1: max(nums[0], nums[1])}

    for house in range(2, len(nums)):
        
        
        maxDict[house] = max(nums[house] + maxDict[house-2], maxDict[house-1])
    
    return maxDict[len(nums)-1]

def robBetter(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    maxIncome = 0

    back2 = nums[0]
    back1 = max(back2, nums[1])

    for house in nums[2:]:

        maxIncome = max(back2 + house, back1)
        back2 = back1
        back1 = maxIncome
    
    return maxIncome

n = [2,1,1,2]

print(robBetter(n))





