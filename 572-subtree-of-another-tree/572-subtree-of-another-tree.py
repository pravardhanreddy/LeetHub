# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def travel(root, subRoot):
            if self.isSameTree(root, subRoot):
                return True
            if root:
                return travel(root.left, subRoot) or travel(root.right, subRoot)
            return False
        return travel(root, subRoot)
            
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pp = collections.deque()
        qq = collections.deque()
        
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        
        pp.append(p)
        qq.append(q)
        
        while pp and qq:
            nodep = pp.popleft()
            nodeq = qq.popleft()
            
            if nodep.val != nodeq.val:
                return False
            
            if nodep.left and nodeq.left:
                pp.append(nodep.left)
                qq.append(nodeq.left)
            elif nodep.left or nodeq.left:
                return False
            if nodep.right and nodeq.right:
                pp.append(nodep.right)
                qq.append(nodeq.right)
            elif nodep.right or nodeq.right:
                return False
        return (len(pp) == 0 and len(qq) == 0)