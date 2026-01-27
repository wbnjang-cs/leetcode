#binaryTreeInOrderTraversal.py
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


def levelOrder(root):
    if root == None:
        return []
    
    d = deque()
    t = deque()
    a = []

    d.append(root)
    
 
    while len(d) != 0:
        level = []
        for node in d:
            level.append(node.val)
            if node.left:
                t.append(node.left)
            if node.right:
                t.append(node.right)
         
        d = t.copy()
        t.clear()
        a.append(level)

    return a

def levelOrderAlternate(root):
    if root == None:
        return []
    
    d = deque()
    d.append(root)
    a = []

    while len(d) != 0:
        level = []
        for i in range(len(d)):
            node = d.popleft()
            level.append(node.val)
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
        
        a.append(level)
    
    return a




    

r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(levelOrderAlternate(r))

