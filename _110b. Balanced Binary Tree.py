# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(root):
            
            # if node in root hasn't got children  
            if root is None:
                return 0
            
            # Once the left sub-tree or right sub-tree is unbalance(the hight difference larger than 1), 
            # the corresponding value will be -1. This section can sop the code and result will be False.
            left  = check(root.left)
            if left == -1:
                return -1
            right = check(root.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
            
        return check(root) != -1
        
