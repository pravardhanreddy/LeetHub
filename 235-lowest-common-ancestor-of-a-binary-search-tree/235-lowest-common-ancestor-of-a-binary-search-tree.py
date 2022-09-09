# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def travel(root,p,q):
            if not root:
                return False, None
            if root is p or root is q:
                return True, root
            
            isFoundLeft, nodeLeft = travel(root.left, p, q)
            if isFoundLeft and nodeLeft is not p and nodeLeft is not q:
                return True, nodeLeft
            isFoundRight, nodeRight = travel(root.right, p, q)
            if isFoundRight and nodeRight is not p and nodeRight is not q:
                return True, nodeRight
            
            if isFoundLeft and isFoundRight:
                return True, root
            
            if isFoundLeft:
                return True, nodeLeft
            if isFoundRight:
                return True, nodeRight
            
            return False, None
        isFound, node = travel(root, p, q)
        return node
            
