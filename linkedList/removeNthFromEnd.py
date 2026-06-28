class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        seen = []
        tempPtr = head
        while tempPtr:
            seen.append(tempPtr.val)
            tempPtr = tempPtr.next
        
        if n == len(seen):
            head = head.next
            return head

        targetIndex = len(seen) - n -1
        currIndex = 0

        prev = head
        removePtr = head.next

        while currIndex < targetIndex and removePtr.next:
            currIndex +=1
            prev = removePtr
            removePtr = removePtr.next
        
        prev.next = removePtr.next

        return head

    def removeNthFromEndBetter(self, head, n):
        temp = 0
        prev = None
        slowPtr = head
        fastPtr = head

        while temp < n:
            fastPtr = fastPtr.next
            temp +=1
        
        while fastPtr.next:
            prev = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        
        if prev == None:
            head = head.next
        else:
            prev.next = slowPtr.next

        return head
    
    def removeNthFromEndAns(self, head, n):
        temp = 0
        dummy = ListNode(-1, head)
        slowPtr = dummy
        fastPtr = dummy

        while temp < n:
            fastPtr = fastPtr.next
            temp +=1
        
        while fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        
        slowPtr.next = slowPtr.next.next
        return dummy.next

        

        
        

# 1. Manually create the nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# 2. Link them together: 1 -> 2 -> 3 -> 4 -> 5
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
head = sol.removeNthFromEndAns(head, 5)

while head:
    print(head.val)
    head = head.next