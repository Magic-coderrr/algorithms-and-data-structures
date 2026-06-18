class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []
            
        result = []
        curr = root

        while curr:
            # If both p and q are greater than curr, we go right side
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                
            # If both p and q are less than curr, we go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                
            # Otherwise, we found the split
            else:
                return curr
                
        