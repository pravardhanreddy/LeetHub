# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sumSoFar = 0
        def travel(root, sumSoFar, B):
            if not root:
                return False
            if root.left == None and root.right == None and sumSoFar + root.val == B:
                return True
            return travel(root.left, sumSoFar + root.val, B) or travel(root.right, sumSoFar + root.val, B)
        return travel(root, sumSoFar, targetSum)