#Notes
#FLoydes Algorith : Finds loops in linked lists.
# 1. Create fast and slow pointers starting at beginning
# 2. send them forward until they meet at same node/point
# 3. Once they meet, send another slow pointer from start, and keep moving slowpointer
# 4. where the two slow pointers meet is the beginning of the loop.

class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

sol = Solution()
l = [1,3,4,2,2]
print(sol.findDuplicate(l))