#Time Complexity : O(n^2)
#Space Complexity : O(n)

def twoSum(nums, target):
    seen = {}
    for index in range(0, len(nums)):
        num = nums[index]
        if target - num in seen:
            return [seen[target-num], index]
        seen[num] = index


nums = [2,7,11,15]
target = 9
        
print(twoSum(nums, target))


