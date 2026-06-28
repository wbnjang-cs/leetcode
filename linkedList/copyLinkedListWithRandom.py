class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        seen = {None : None}
        oldPtr = head
        while oldPtr:
            temp = Node(oldPtr.val, None, None)
            seen[oldPtr] = temp
            oldPtr = oldPtr.next

        oldPtr = head
        while oldPtr:
            newPtr = seen[oldPtr]
            newPtr.next = seen[oldPtr.next]
            newPtr.random = seen[oldPtr.random]
            oldPtr = oldPtr.next

        return seen[head]













#===========================================================================
def LinkList(l):
    head = Node(l[0], None, None)
    prev = head

    for num in l[1:]:
        temp = Node(num, None, None)
        prev.next = temp
        prev = prev.next

    return head

def printLinked(h):
    print("list is : ")
    while h:
        print(h.val)
        h = h.next

        
l = [1,2,3,4]
h = LinkList(l)

sol = Solution()

newH = sol.copyRandomList(h)
printLinked(newH)


