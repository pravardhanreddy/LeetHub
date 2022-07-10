# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isBalanced(self, A):
        def helper(A):
            if not A:
                return 0
            
            lh = helper(A.left)
            rh = helper(A.right)
            
            if lh is False or rh is False:
                return False
            
            if abs(lh-rh) > 1:
                return False
            else:
                return 1 + max(lh,rh)
        return False if helper(A) is False else True
        