# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        
        newHead = head

        leadNode = head.next
        tempPtr = leadNode

        newHead.next = None

        while tempPtr != None:
            tempPtr = tempPtr.next
            leadNode.next = newHead
            newHead = leadNode
            leadNode = tempPtr
        
        return newHead
        


# Create the individual nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link them together: 1 -> 2 -> 3 -> 4 -> 5 -> None
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# The 'head' of the list is node1
head = node1

mysol = Solution()
mysol.reverseList(head)