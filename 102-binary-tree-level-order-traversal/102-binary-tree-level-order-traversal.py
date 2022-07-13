# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = dict()
        h = 0
        maxh = [-1]
        def travel(root, h, maxh, d):
            if not root:
                return
            if h > maxh[0]:
                maxh[0] = h
                d[h] = [root.val]
            else:
                d[h].append(root.val)
            travel(root.left, h+1, maxh, d)
            travel(root.right, h+1, maxh, d)
        travel(root, h, maxh, d)
        return [d[i] for i in range(maxh[0] + 1)]
        
            
        
            