# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        h = 0
        d = {}
        q = deque()
        q.append((root,h))
        
        while len(q):
            curr, h = q.popleft()
            if h >= len(d):
                d[h] = []
            d[h].append(curr.val)
            
            if curr.left:
                q.append((curr.left, h+1))
            if curr.right:
                q.append((curr.right, h+1))
        ans = []
        for i in range(len(d)):
            ans.append(d[i] if i%2 == 0 else reversed(d[i]))
            d.pop(i)
        return ans