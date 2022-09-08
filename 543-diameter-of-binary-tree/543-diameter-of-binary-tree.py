# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def travel(root, maxd):
            if not root:
                return 0
            hl = travel(root.left, maxd)
            hr = travel(root.right, maxd)
            maxd[0] = max(maxd[0], hl+hr)
            return max(hl, hr) + 1
        
        maxd = [0]
        travel(root, maxd)
        return maxd[0]