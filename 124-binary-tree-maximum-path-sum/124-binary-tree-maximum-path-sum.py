# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def travel(root):
            if root.left and root.right:
                lmax, lpath = travel(root.left)
                rmax, rpath = travel(root.right)

                return max([root.val, lmax, rmax, lpath + root.val, rpath + root.val, lpath + rpath + root.val]), max([root.val, lpath + root.val, rpath + root.val])
            if root.left:
                lmax, lpath = travel(root.left)
                return max([root.val, lmax, lpath + root.val]), max(lpath + root.val, root.val)
            if root.right:
                rmax, rpath = travel(root.right)
                return max([root.val, rmax, rpath + root.val]), max(rpath + root.val, root.val)
            
            return root.val,root.val

        
        return travel(root)[0]