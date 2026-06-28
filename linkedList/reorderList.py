class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        sPtr = head
        fPtr = head.next

        while fPtr and fPtr.next:
            sPtr = sPtr.next
            fPtr = fPtr.next.next
        
        if sPtr.next:
            backHead = sPtr.next
            sPtr.next = None

            if backHead.next:
                lead = backHead.next
                backHead.next = None
                while lead:
                    curr = lead
                    lead = lead.next
                    curr.next = backHead
                    backHead = curr
            
            while head and backHead:
                currFront = head
                head = head.next
                currBack = backHead
                backHead = backHead.next

                currFront.next = currBack
                currBack.next = head
    
    def reorderListAns(self, head):
        sPtr = head
        fPtr = head

        #find half
        while fPtr and fPtr.next:
            sPtr = sPtr.next
            fPtr = fPtr.next.next
        
        backHead = sPtr.next
        sPtr.next = None
        prev = None

        #reverse second half
        while backHead:
            lead = backHead.next
            backHead.next = prev
            prev = backHead
            backHead = lead
        

        #prev is where the actual new head is stored
        backHead = prev

        #merge two halfs
        while backHead:
            nextFront, nextBack = head.next, backHead.next

            head.next = backHead
            backHead.next = nextFront

            head, backHead = nextFront, nextBack



        


        

            


        
        




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
sol.reorderListAns(head)

while head:
    print(head.val)
    head = head.next