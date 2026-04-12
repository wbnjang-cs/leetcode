import heapq
from collections import defaultdict
from collections import deque

def maxSlidingWindow(nums, k):
    l =  0
    r = k

    res = []

    currWindow = defaultdict(int)

    heap = []
    heapq.heapify(heap)
    for r in range(k):
        currWindow[nums[r]] +=1
        heapq.heappush(heap, -nums[r])

    res.append(-heap[0])

    for r in range(k, len(nums)):
        currWindow[nums[r]] +=1
        currWindow[nums[l]] -=1
        
        while heap and currWindow[-heap[0]] == 0:
            heapq.heappop(heap)
            
        heapq.heappush(heap, -nums[r])

        res.append(-heap[0])

        l +=1
    
    return res

def maxSlidingWindowAns(nums, k):
    result = []
    #q will store indexes, and it will be decreasing in terms of the numbers the indexes represent
    q = deque([])

    #build the que for the first window
    for r in range(k):
        #Keep popping while the last element is smaller than or equal to int you are putting in
        #[9,7,6], 8 -> [9,8]
        while q and nums[r] >= nums[q[-1]]:
            q.pop()
        q.append(r)
    
    #first in q is the biggest in current window
    result.append(nums[q[0]])

    #We completed q for first window, second window starts from l=1
    l = 1

    for r in range(k, len(nums)):
        #same logic, pop as log as current num is >= last num in que
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        
        #if biggest element is out of window, remove it
        if l > q[0]:
            q.popleft()

        result.append(nums[q[0]])
        l +=1

    return result