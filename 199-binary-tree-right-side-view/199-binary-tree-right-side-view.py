# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        ans = []
        q.append(root)
        while q:
            n = len(q)
            while n > 1:
                node = q.popleft()
                n -= 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            node = q.popleft()
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
                    