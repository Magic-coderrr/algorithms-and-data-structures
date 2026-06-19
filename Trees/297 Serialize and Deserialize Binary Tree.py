# Serialization is the process of converting a data structure or object into a sequence of bits so 
# that it can be stored in a file or memory buffer, or transmitted across a network connection link 
# to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how
# your serialization/deserialization algorithm should work. You just need to ensure that a binary 
# tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
# You do not necessarily need to follow this format, so please be creative and come up with 
# different approaches yourself.
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
            
        res = []
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Is it a real node or none if real we appends its val else we append N directly to res list
            if node:
                res.append(str(node.val)) 
                queue.append(node.left)   # Pushing left child (even if its None)
                queue.append(node.right)  # Pushing right child (even if its None)
                
            else:
                res.append("N") 
 
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        i = 1
        
        while queue:
            # Pop the parent node from the queue
            parent = queue.popleft()
            
            # Processing the left child
            if vals[i] != "N":
                nod = TreeNode(int(vals[i]))
                parent.left = nod
                queue.append(nod)
            i += 1  
            
            # Processing the right child
            if vals[i] != "N":
                nod = TreeNode(int(vals[i]))
                parent.right = nod
                queue.append(nod)
            i += 1  
            
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))