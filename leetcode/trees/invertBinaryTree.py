class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None
    
    tempr = root.right

    root.right = invertTree(root.left)
    root.left = invertTree(tempr)

    return root

def invertTreeClean(root):
    if not root:
        return None
    
    root.left, root.right = (invertTree(root.right), invertTree(root.left))


