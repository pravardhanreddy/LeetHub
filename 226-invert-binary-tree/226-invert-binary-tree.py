# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, A: Optional[TreeNode]) -> Optional[TreeNode]:
        if not A:
            return
        A.left, A.right = A.right, A.left
        self.invertTree(A.left)
        self.invertTree(A.right)
        return A