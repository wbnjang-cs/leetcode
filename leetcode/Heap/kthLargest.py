import heapq

def findKthLargest(nums,k):
    h = []

    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    
    return h[0]

    
    

nums = [3,2,3,1,2,4,5,5,6]
k = 4

print(findKthLargest(nums, k))