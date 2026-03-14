import heapq
from collections import Counter

def topKFrequent(nums, k):
    if len(nums) == 0:
        return []
    
    seen = {}
    ans = []
    ret = []
    heapq.heapify(ans)
    for num in nums:
        if num not in seen:
            seen[num] = 0
        seen[num] +=1
    
    for key, value in seen.items():
        heapq.heappush(ans, (value, key))
        if len(ans) > k:
            heapq.heappop(ans)

    for pair in ans:
        ret.append(pair[1])
    
    return ret

def topKFrequentSimple(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

def topKFrequentBest(nums, k):
    count = Counter(nums)

    buckets = [[] for x in range(len(nums)+1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    res = []

    for i in range(len(buckets)-1, 0, -1):
        for n in buckets[i]:
            res.append(n)
            if len(res) == k:
                return res
    

    



nums = [1,2,1,2,1,2,3,1,3,2]
k=2

print(topKFrequent(nums, k))

    
