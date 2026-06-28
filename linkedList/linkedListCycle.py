class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slowPtr = head
        fastPtr = head

        while fastPtr != None:
            if fastPtr.next == None:
                return False
            else:
                fastPtr = fastPtr.next.next
            
            slowPtr = slowPtr.next

            if fastPtr == slowPtr:
                return True
        
        return False
        