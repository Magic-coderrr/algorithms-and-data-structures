# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
# binary tree and inorder is the inorder traversal of the same tree, construct and return the 
# binary tree.
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        # If the arrays are empty we just return none
        if not preorder or not inorder:
            return None
            
        # Grabbing the root value and creating the node
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Finding the split point in the inorder array before that everything will be left side and rest in right side
        mid = inorder.index(root_val)
        
        # Building the left subtree Passing the sliced preorder and sliced inorder
        # Left preorder: starts at index 1, takes 'mid' elements -> [1 : mid+1]
        # Left inorder: everything up to 'mid' -> [:mid]
        root.left = self.buildTree(preorder[1 : mid+1], inorder[ : mid])
        
        # Building the right subtree
        root.right = self.buildTree(preorder[mid+1 : ], inorder[mid+1 : ])
        
        return root