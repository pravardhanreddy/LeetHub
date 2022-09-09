# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def travel(root):
            minL, maxR = 0, 0
            if root.left:
                isvalidL, minL, maxL = travel(root.left)
                if not isvalidL or maxL >= root.val:
                    return False, 0, 0
            
            if root.right:
                isvalidR, minR, maxR = travel(root.right)
                if not isvalidR or minR <= root.val:
                    return False, 0, 0
            
            if root.left and root.right:
                return True, minL, maxR
            
            if root.left:
                return True, minL, root.val
            if root.right:
                return True, root.val, maxR
            return True, root.val, root.val 
        
        return travel(root)[0]