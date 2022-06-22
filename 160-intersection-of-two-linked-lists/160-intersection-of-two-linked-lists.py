# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while not (a == None and b == None):
            if a == None:
                a = headB
            if b == None:
                b = headA
            if a == b:
                return a
            a = a.next
            b = b.next
        return None