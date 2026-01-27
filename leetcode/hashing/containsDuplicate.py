def containsDuplicate(nums):
    d = {}
    for num in nums:
        if num in d:
            return True
        d[num] = 1
    
    return False

def containsDuplicateFaster(nums):
    return len(nums) != len(set(nums))
    #while this could be faster, it has to check every element, so it might be slower because there are no early exits

def containsDuplicateFasterHybrid(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def containsDuplicateResolve(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False