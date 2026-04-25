def search(nums, target):
    if target < nums[0] or target > nums[-1]:
        return -1
    
    if len(nums) == 1:
        return 0 if target == nums[0] else -1
    
    i = 0
    j = len(nums) -1

    while i <= j:
        #should be i + (j-i) // 2 to prevent integer overflow 
        s = (j + i) // 2
        if target == nums[s]:
            return s
        elif target > nums[s]:
            i = s + 1
        elif target < nums[s]:
            j = s - 1

    return -1

    
n = [-1,0,3,5,9,12]
t = 9

n2 = [-1,0,3,5,9,12]
t2 = 2

n3 = [5]
t3 = 5

n4 = [2,5]
t4 = 5

print(search(n, t))
print(search(n2, t2))
print(search(n3, t3))
print(search(n4, t4))