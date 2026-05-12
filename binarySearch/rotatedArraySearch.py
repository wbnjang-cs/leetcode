def search(nums, target):
    i = 0
    j = len(nums) -1

    while i <= j:
        m = i + (j-i) // 2 
        if nums[m] == target:
            return m
        
        #nums[i] is smallest, nums[m] is biggest in left side
        #important*********************
        #has to be <=, NOT <.
        #If i == m, then we will use right side sorted logic when left side is sorted (1 element is always sorted)
        #Basically using < when i == m assumes that a single element is not sorted and goes to wrong logic
        if nums[i] <= nums[m]:
        #important*********************
            if nums[m] < target or nums[i] > target:
                i = m + 1
            else:
                j = m - 1
        #nums[m] is smallest, nums[j] is biggest
        else:
            if nums[m] > target or nums[j] < target:
                j = m - 1
            else:
                i = m + 1
        
    
    return -1

def searchRe(nums, target):
    i = 0
    j = len(nums) - 1

    while i <= j:
        m = i + (j - i) // 2
        if nums[m] == target:
            return m
        
        #left side is sorted
        if nums[i] <= nums[m]:
            #target should be inside left side if exists
            if nums[i] <= target and target <= nums[m]:
                j = m - 1
            else:
                i = m + 1
        
        #right side sorted
        else:
            #target should be inside right side if exists
            if nums[m] <= target and target <= nums[j]:
                i = m + 1
            else:
                j = m - 1

    return -1




n1 = [4,5,6,7,0,1,2]
t1 = 0
print(searchRe(n1, t1))

n3 = [3,5,6,0,1,2]
t3 = 5
print(searchRe(n3, t3))

n2=[3, 1]
t2=1
print(searchRe(n2, t2))