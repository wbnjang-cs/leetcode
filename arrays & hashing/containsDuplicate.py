def containsDuplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = 1

    return False

def containsDuplicateBetter(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
    return False

def containsDuplicateBetter(nums):
    if len(nums) != len(set(nums)):
        return True
    return False