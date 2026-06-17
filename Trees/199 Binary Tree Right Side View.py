# Given the root of a binary tree, imagine yourself standing on the right side of it,
#  return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
            
        result = []
        q = deque([root])
        
        while q:
            length = len(q)
            
            for i in range(length):
                popped = q.popleft()
                
                # If this is the very last node of the current level loop
                if i == length - 1:
                    # Append its Value directly to our final result array/list
                    result.append(popped.val)
                
                # Keep pushing children to the queue normally
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                    
        return result