# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        h = 1
        def order(root, ans, h):
            if not root:
                return
            if h > len(ans):
                ans.append(root.val)
            order(root.right, ans, h+1)
            order(root.left, ans, h+1)
        order(root, ans, h)
        return ans