# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):
        if not root:
            return
        stack = []
        curr = root
        while curr:
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                curr.right = curr.left
                curr.left = None
                curr = curr.right
                continue
            if len(stack):
                curr.right = stack.pop()
                curr = curr.right
            else:
                break
        return root
        