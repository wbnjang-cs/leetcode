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
    #Key idea is to sort the array first, then fix the first value
    #and use two pointer two sum to find the other 2 number in the triplet
    nums.sort()
    result = []


    #We go through the array. j = i+1 and j<k would catch errors
    #from i < len(nums) but this technically right
    i = 0
    while i < len(nums) -2:
        #Whenever there is a duplicate in the first value, 
        #it will create a duplicate valid triplet. So we skip
        start = nums[i]
        if i > 0 and start == nums[i-1]:
            i +=1
            continue
        

        target = 0 - start
        #If target is smaller than start, it does not exist,
        #and it will never exist for any numbers bigger than us.
        if target < start:
            break

        #twosum twopointer for sorted array
        j = i + 1
        k = len(nums) - 1

        #if left bound right of right bound, we stop
        while j < k:
            #j is left bound (smaller num since sorted)
            #k is right bound (bigger num since sorted)
            curr_sum = nums[j] + nums[k]
            #sum too big -> bigger num should be smaller
            if curr_sum > target:
                k -=1
            #sum too small -> smaller num should be bigger
            elif curr_sum < target:
                j +=1
            #if sum == target we add the result to result list
            #and adjust bounds
            else:
                result.append([nums[i], nums[j], nums[k]])
                j +=1
                #if second element has duplicates,
                #this will also cause duplicate valid triplets
                #so we move j until it is no longer a duplicate
                while j < k and nums[j] == nums[j-1]:
                    j +=1
                #since k is directly related to i and j,
                #ensuring no duplicates there ensures k
                #is fine
        i +=1

    return result




            


n = [-1,0,1,2,-1,-4] # [-4, -1, -1, 0, 1, 2]
n1 = [0,0,0]
n2 = [0,1,1]
print(threeSumAns(n))

n3 = [-1,0,1,0]
print(threeSum(n3))
