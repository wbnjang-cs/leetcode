#binaryTreeInOrderTraversal.py


from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    answer = []

    inorderRecursive(root, answer)

    return answer

def inorderRecursive(root, ans):
    if not root:
        return
    
    if root.left:
        inorderRecursive(root.left, ans)
    
    ans.append(root.val)

    if root.right:
        inorderRecursive(root.right, ans)


def inorderTraversalIterative(root):
    ans = []
    d = deque()
    d.append(root)

    while d:
        n = d.popleft()
        if not n:
            continue
        if not n.left:
            ans.append(n.val)
            d.appendleft(n.right)
            continue


        l = n.left
        n.left = None
        d.appendleft(n)
        d.appendleft(l)
    return ans
        




#---------------------------------------------------------------


#slightly faster/cleaner, same bit ) memory and runtime, so don't sweat it.
def inorderTraversalOptimized(root):
    ans = []

    def inorderRec(root):
        if not root:
            return
        inorderRec(root.left)
        ans.append(root.val)
        inorderRec(root.right)

    inorderRec(root)

    return ans


n9 = TreeNode(9)

n6 = TreeNode(6)
n7 = TreeNode(7)

n4 = TreeNode(4)
n5 = TreeNode(5, left=n6, right=n7)

n8 = TreeNode(8, left = n9)

n2 = TreeNode(2, left=n4, right=n5)
n3 = TreeNode(3, right=n8)

root = TreeNode(1, left=n2, right=n3)

print(inorderTraversalIterative(root))

