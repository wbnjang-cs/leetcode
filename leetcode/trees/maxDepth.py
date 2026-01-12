def maxDepth(root):
    if root == None:
        return 0
    elif not root.left and not root.right:
        return 1
    else:
        return max(maxDepth(root.left), maxDepth(root.right))
    
def maxDepthBetter(root):
    if not root:
        return 0
    return max(maxDepthBetter(root.right), maxDepthBetter(root.left)) + 1