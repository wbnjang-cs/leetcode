def findMin(nums):
    i = 0
    j = len(nums) -1
    min = nums[0]

    while i <= j:
        m = i + (j-i) // 2
        if nums[m] < min:
            min = nums[m]

        if nums[m] < nums[j]:
            j = m-1
        else:
            i = m+1

    return min

#same logic as my ans, has early exit
def findMinAns(nums):
    i = 0
    j = len(nums) -1
    smallest = nums[0]

    #This accounts for array not being rotated
    while i <= j:
        #This means the boundary is sorted. The smallest number is either the start of this array (i) or one past the boundary (previous m, j + 1)
        #EX:  i = 0, j = 3
        #EX:  i = 4, j = 6, j + 1 = 7 (got here by j = m - 1)
        if nums[i] < nums[j]:
            smallest = min(smallest, nums[i])
            break

        m = (i + j) // 2
        smallest = min(smallest, nums[m])
        if nums[i] <= nums[m]:
            i = m + 1
        else:
            j = m - 1

    return smallest
    

n1 = [3,4,5,1,2]
print(findMin(n1))

n2 = [4,5,6,7,0,1,2]
print(findMin(n2))

n3 = [5,1,2,3,4]
print(findMin(n3))

n4 = [3,4,5,6,1,2]
print(findMin(n4))