class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution(object):
    

    def reverseKGroup(self, head, k):
        count = 1

        dummyNode = ListNode(-1, head)
        lagPtr = head
        leadPtr = head
        prevHead = dummyNode
        

        while leadPtr:
            
            if count == k:

                prevHead.next = leadPtr
                prevHead = lagPtr

                leadPtr = leadPtr.next
                
                endNode = leadPtr
                
                nextNode = endNode
                
                while lagPtr != endNode:
                    tempPtr = lagPtr
                    lagPtr = lagPtr.next
                    tempPtr.next = nextNode
                    nextNode = tempPtr

                count = 1


            else:

                leadPtr = leadPtr.next
                count +=1
            
        return dummyNode.next

        


# --- Helper functions to test the code ---

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print("[" + ",".join(result) + "]")


# --- Executing the Test Case ---
if __name__ == "__main__":
    # Define example inputs from the image
    input_array = [1,2,3,4,5,6,7]
    k = 3
    
    # 1. Initialize the linked list
    head = create_linked_list(input_array)
    
    # 2. Instantiate your solution class 
    # (Assumes your class is named 'Solution' and method is 'reverseKGroup')
    sol = Solution()
    modified_head = sol.reverseKGroup(head, k)
    
    # 3. Print the output to verify
    print("Output:")
    print_linked_list(modified_head)