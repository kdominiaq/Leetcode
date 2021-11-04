import numpy as np

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = np.array([], int)
        while root:
            value = root.val
            result = np.append(result, value)
            
            root = root.right
        
        return result
