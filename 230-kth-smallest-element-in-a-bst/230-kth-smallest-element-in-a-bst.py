# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
n = 0
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer

    def kthSmallest(self, A, B):
        global n
        n = B
        def dfs(A):
            global n
            if not A:
                return A
            ans = dfs(A.left)
            if ans != None:
                return ans
            n -= 1
            if n == 0:
                return A.val
            ans = dfs(A.right)
            if ans != None:
                return ans
        
        return dfs(A)
        