def threeSum(nums):
    nums.sort()
    result = []

    i = 0

    while i < len(nums):
        start = nums[i]
        target = 0 - start
        if target < start:
            break

        j = i + 1
        k = len(nums) - 1

        while j < k:
            sum = nums[j] + nums[k]
            if sum > target:
                k -=1
            elif sum < target:
                j +=1
            else:
                ans = [nums[i], nums[j], nums[k]]
                if ans not in result:
                    result.append(ans)
                j +=1
        
        i +=1

    return result

def threeSumAns(nums):
    nums.sort()
    result = []

    i = 0
    while i < len(nums):
        start = nums[i]
        #If we have started with this value before, It will cause duplicates. so skip it
        #Had to learn from hint
        if i > 0 and start == nums[i-1]:
            i +=1
            continue

        target = 0 - start
        #If target is smaller than start, it does not exist, and it will never exist for any numbers bigger than us.
        if target < start:
            break

        #twosum twopointer for sorted array
        j = i + 1
        k = len(nums) - 1

        while j < k:
            sum = nums[j] + nums[k]
            if sum > target:
                k -=1
            elif sum < target:
                j +=1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j +=1
                while j < k and nums[j] == nums[j-1]:
                    j +=1
        i +=1

    return result




            


n = [-1,0,1,2,-1,-4] # [-4, -1, -1, 0, 1, 2]
n1 = [0,0,0]
n2 = [0,1,1]
print(threeSum(n))

n3 = [-1,0,1,0]
print(threeSum(n3))
