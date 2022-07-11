# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cmp_to_key
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        v = 0
        least = [0]
        d = {}
        h = 0
        
        def compare(x,y):
            if x[1] > y[1]:
                return 1
            elif x[1] == y[1]:
                return 1 if x[0] > y[0] else -1
            return -1
                
        
        def travel(root, v, h, least, d):
            if not root:
                return
            if v not in d:
                if v < least[0]:
                    least[0] = v
                d[v] = [[root.val,h]]
            else:
                d[v].append([root.val,h])
            travel(root.left, v-1, h+1, least, d)
            travel(root.right, v+1, h+1, least, d)
        travel(root, v, h, least, d)
        least = least[0]
        ans = []
        while least in d:
            l = d[least]
            least += 1
            l.sort(key=cmp_to_key(compare))
            ans.append([x[0] for x in l])
        return ans