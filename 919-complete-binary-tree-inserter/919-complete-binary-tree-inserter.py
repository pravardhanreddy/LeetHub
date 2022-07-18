# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()
        self.q.append(self.root)
        while self.q[0].left and self.q[0].right:
            top = self.q.popleft()
            self.q.append(top.left)
            self.q.append(top.right)
        if self.q[0].left:
            self.q.append(self.q[0].left)

    def insert(self, val: int) -> int:
        
        node = self.q.popleft()
        if node.left:
            node.right = TreeNode(val)
            self.q.append(node.right)
            return node.val
        
        node.left = TreeNode(val)
        self.q.appendleft(node)
        self.q.append(node.left)
        return node.val

        
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()