def longestConsecutive(nums):
    seen = {}
    longest = 0
    

    for num in nums:
        if num in seen:
            continue

        if num not in seen:
            seen[num] = [num]
            longest = max(longest, len(seen[num]))
        
        if num - 1 in seen:
            seen[num] = seen[num-1] + seen[num]
            seen[seen[num][0]] = seen[num]
            longest = max(longest, len(seen[num]))
            
        
        if num+1 in seen:
            
            seen[num+1] = seen[num] + seen[num+1]
            seen[seen[num+1][-1]] = seen[num+1]
            seen[seen[num][0]] = seen[num+1]
            longest = max(longest, len(seen[num+1]))
            
    return longest  
    print(seen)
    print(longest)

def longestConsecutiveAnswer(nums):
    nums = set(nums)
    longest = 0

    for n in nums:
        if n-1 not in nums:
            length = 0
            while (n+length) in nums:
                length +=1
            longest = max(length, longest)
    return longest



    

nums1 = [5, 2,20,4,10,3,4,]
nums2 = [0,3,2,5,4,6,1,1]
nums3=[100,4,200,1,3,2]

print(longestConsecutiveAnswer(nums2))