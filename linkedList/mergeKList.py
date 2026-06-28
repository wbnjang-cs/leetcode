class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLists(l1, l2):
    sentNode = ListNode(-1)
    temp = sentNode
    h1 = l1
    h2 = l2

    while h1 and h2:
        if h1.val < h2.val:
            temp.next = h1
            h1 = h1.next
        else:
            temp.next = h2
            h2 = h2.next
        
        temp = temp.next
    
    while h1:
        temp.next = h1
        h1 = h1.next
        temp = temp.next
    
    while h2:
        temp.next = h2
        h2 = h2.next
        temp = temp.next
    
    return sentNode.next

    
class Solution:
    def mergeKLists(self, lists):
        i = 0
        h1 = None

        while i < len(lists):
            
            if lists[i]:
                h1 = lists[i]
                i +=1
                break
            
            i +=1


        while i < len(lists):
            if lists[i]:
                h1 = mergeLists(h1, lists[i])

                i +=1
                continue
            print("adding")
            i +=1
        
        return h1
    
    def mergeKListsAns(self, lists):
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                h1 = lists[i]
                h2 = lists[i+1] if (i+1) < len(lists) else None

                mergedLists.append(mergeLists(h1, h2))
            
            lists = mergedLists
        
        return lists[0]


