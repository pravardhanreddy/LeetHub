# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def height(self, root):
        if not root:
            return 0
        return 1+(self.height(root.left) + self.height(root.right))
        
    def levelOrderBottom(self, A):
        if not A:
            return []
        # ans = [[] for i in range(self.height(A))]
        ans = []
        h = 0
        def travel(root, ans, h):
            if not root:
                return
            if h == len(ans):
                ans.append([])
            ans[h].append(root.val)
            h += 1
            travel(root.left, ans, h)
            travel(root.right, ans, h)
        
        travel(A, ans, h)
        while len(ans[-1]) == 0:
            ans.pop()
        return reversed(ans)
        