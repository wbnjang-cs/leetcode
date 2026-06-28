
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if not list1 and not list2:
            return None

        l = list1
        r = list2

        if l == None:
            tempPtr = r
            r = r.next
        elif r == None:
            tempPtr = l
            l = l.next
        elif l.val <= r.val:
            tempPtr = l
            l = l.next
        elif l.val > r.val:
            tempPtr = r
            r = r.next
        
        newHead = tempPtr

        while l != None and r != None:
            if l.val <= r.val:
                tempPtr.next = l
                tempPtr = tempPtr.next
                l = l.next
            else:
                tempPtr.next = r
                tempPtr = tempPtr.next
                r = r.next
        
        while l != None:
            tempPtr.next = l
            tempPtr = tempPtr.next
            l = l.next
        while r != None:
            tempPtr.next = r
            tempPtr = tempPtr.next
            r = r.next

        
        return newHead
    
    def mergeTwoListsAns(self, list1, list2):
        newHeadPrev = ListNode()
        tempPtr = newHeadPrev



        while list1 and list2:
            if list1.val <= list2.val:
                tempPtr.next = list1
                list1 = list1.next
            else:
                tempPtr.next = list2
                list2 = list2.next
            
            tempPtr = tempPtr.next
        
        if list1:
            tempPtr.next = list1
        if list2:
            tempPtr.next = list2

        
        return newHeadPrev.next

























#=================================================================================================
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)


list1 = build_linked_list([2,5,7])
list2 = build_linked_list([1, 3, 4])

solution = Solution()
head = solution.mergeTwoListsAns(list1, list2)


print("Output:")
print_linked_list(head)
