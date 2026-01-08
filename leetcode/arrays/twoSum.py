#Time Complexity : O(n^2)
#Space Complexity : O(n)

def twoSum(nums, target):
    ans = []
    hashT = {}
    for x in range(len(nums)):
        hashT[x] = nums[x]
    
    i = 0
    for x in nums:
        if (target-x) in hashT.values() and (target-x) in nums[i+1:]:
            ans.append(i)
            ans.append(nums.index(target-x, i+1))
            return ans
        i+=1


def twoSumAnswer(nums, target):
    #we make a dictionary
    hash_map = {} 
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num] = i
            


def twoSumResolve(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [i, seen[complement]]
        seen[value] = i



