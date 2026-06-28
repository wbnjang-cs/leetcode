class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prevNode = ListNode(l1.val + l2.val)
        newHead = prevNode
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            currNode = ListNode(l1.val + l2.val)
            prevNode.next = currNode
            prevNode = prevNode.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            currNode = ListNode(l1.val)
            prevNode.next = currNode
            prevNode = prevNode.next
            l1 = l1.next

        while l2:
            currNode = ListNode(l2.val)
            prevNode.next = currNode
            prevNode = prevNode.next
            l2 = l2.next
        
        temp = newHead
        while temp:
            if temp.val >= 10:
                if not temp.next:
                    temp.next = ListNode(0)
                temp.next.val +=1
                temp.val -=10
            temp = temp.next
    
        return newHead

    def addTwoNumbersAns(self, l1, l2):
        beforeHead = ListNode(0)
        prevNode = beforeHead
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            nodeVal = total % 10

            currNode = ListNode(nodeVal)

            prevNode.next = currNode
            prevNode = prevNode.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return beforeHead.next




            


#===========================================================================
def LinkList(l):
    head = ListNode(l[0], None)
    prev = head

    for num in l[1:]:
        temp = ListNode(num, None)
        prev.next = temp
        prev = prev.next

    return head

def printLinked(h):
    print("list is : ")
    while h:
        print(h.val)
        h = h.next

l1 = [9]
h1 = LinkList(l1)

l2 = [9]
h2 = LinkList(l2)

sol = Solution()
h3 = sol.addTwoNumbersAns(h1, h2)

printLinked(h3)

