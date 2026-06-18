# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the 
# sequence has an edge connecting them. A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, returnxxx the maximum path sum of any non-empty path.
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        
        # Post-Order DFS as we would start from leaves 
        def dfs(node):
            if not node:
                return 0 
                
            # Diving down to leaves, pruning negative branches with max(..., 0)
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # The Global Record 
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)
            
            # going to the branch which is max as highest sum would be there
            return node.val + max(left_max, right_max)
            
        dfs(root)
        
        return self.max_sum
        