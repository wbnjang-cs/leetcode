def productExceptSelf(nums):
    productDict = {}
    zeroCount = 0
    totalProduct = 1
    res=[0] * len(nums)

    for i in range(len(nums)):
        if nums[i] == 0:
            zeroCount +=1
            zeroLoc = i
            if zeroCount == 2:
                return res
            continue

        totalProduct *= nums[i]
    
    if zeroCount == 1:
        res[zeroLoc] = totalProduct
    else:
        for i in range(len(nums)):
            res[i] = totalProduct // nums[i]
    
    return res

def productExceptSelfBetter(nums):

    prefix = 1
    postfix = 1
    res = [1] * len(nums)

    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res

    

nums = [1,2,4,6]

print(productExceptSelfBetter(nums))