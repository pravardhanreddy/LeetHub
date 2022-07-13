# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, A):
        if not A:
            return True
        ql = deque()
        qr = deque()
        
        ql.append(A.left)
        qr.append(A.right)
        
        while len(ql) and len(qr):
            l = ql.popleft()
            r = qr.popleft()
            
            if l and r:
                if l.val == r.val:
                    ql.append(l.left)
                    ql.append(l.right)
                    
                    qr.append(r.right)
                    qr.append(r.left)
                else:
                    return False
            elif l or r:
                return False
        return True
        