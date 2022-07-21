"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        root = Node(0)
        d = dict()
        dr = dict()
        temp = head
        new_root = root
        i = 0
        while temp:
            d[temp] = i
            root.next = Node(temp.val)
            root = root.next
            dr[i] = root
            temp = temp.next
            i += 1
        
        temp = head
        root = new_root.next
        
        i = 0
        while temp:
            if temp.random:
                ind = d[temp.random]
                root.random = dr[ind]
            i += 1
            root = root.next
            temp = temp.next
        return new_root.next