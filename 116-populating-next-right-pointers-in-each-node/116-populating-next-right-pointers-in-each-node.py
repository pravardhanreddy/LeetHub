"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        root.next = None # This is always the case
        curr = root
        next_node = None # First node to visit in the next level
        
        while curr or next_node:
            if curr:
                if curr.left and curr.right: # Connect the children if both exist
                    curr.left.next = curr.right
                    
                if curr.left or curr.right: # Atleast one child is present
                    child = curr.right if curr.right else curr.left    
                    t = curr.next # Find the next node with children
                    while t and not (t.left or t.right):
                        t = t.next
                        
                    if not t: # Reached None (this means after curr there are no nodes with children)
                        child.next = None # This is the last node in the child's level
                    else:
                        child.next = t.left if t.left else t.right
                    
                    # If next_node is empty that means we just started a new level and curr has atleast one child
                    if not next_node: 
                        next_node = curr.left if curr.left else curr.right
                # For the case where curr has no children, there's nothing to do
                curr = curr.next # Move to the next node
            else:
                curr = next_node
                next_node = None
        return root