from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        level = 0
        
        while queue:
            # increase the level by 1 because another level exists
            level += 1
            
            # number of exist roots (0, 1 or 2)
            b = len(queue)

            
            for root in range(b):
                # delete the first given root from queue
                rt = queue.popleft()
                
                # if parent root has child (left or right) then add this root ro queue
                if rt.left:
                    queue.append(rt.left)
                if rt.right:
                    queue.append(rt.right)
                    
                # if root has not got child, then return level (because it's the last layer where root exists)
                if not rt.left and not rt.right:
                    return level
                
        return -1
