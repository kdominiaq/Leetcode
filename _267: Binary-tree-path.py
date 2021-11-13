import numpy as np
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:          
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if root is empty
        if not root: 
            return []
            
        # left parh
        result= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.left)]
        
        # right path
        result+= [ str(root.val)+"->" + path for path in self.binaryTreePaths(root.right)]
                
        return result or [str(root.val)] 
