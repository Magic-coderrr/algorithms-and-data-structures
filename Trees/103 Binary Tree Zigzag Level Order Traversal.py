# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
#  (i.e., from left to right, then right to left for the next level and alternate between).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]


from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
            
        result = []
        q = deque([root])
        left_to_right = True
        
        while q:
            length = len(q)
            temp_lst = []
            for i in range(length):
                popped = q.popleft()
               
                # Append its Value directly to our final result array/list
                temp_lst.append(popped.val)
                
                # Keep pushing children to the queue 
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

            # 1. Check the flag to decide How we append
            if left_to_right:
                result.append(temp_lst)          # Appending normally
            else:
                result.append(temp_lst[::-1])    # Appending reversed

            # 2. Flipping the switch for the next level
            left_to_right = not left_to_right
                    
        return result