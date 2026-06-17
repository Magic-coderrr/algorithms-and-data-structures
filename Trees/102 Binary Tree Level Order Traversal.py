# Given the root of a binary tree, return the level order traversal of its nodes' 
# values. (i.e., from left to right, level by level).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
            
        result = []
        q = deque([root])
        
        while q:
            length = len(q)
            temp_lst = []  # Standard list for the level's values like if its on level 2 it will store that levels values
            
            for i in range(length):
                popped = q.popleft()
                
                # 1. Appending the Value
                temp_lst.append(popped.val)
                
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                    
            # Adding this level's completed list to the final result
            result.append(temp_lst)
            
        return result