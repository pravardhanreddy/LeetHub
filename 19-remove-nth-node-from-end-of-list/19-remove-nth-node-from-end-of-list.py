# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, A, B):
        first = A
        if not first.next:
            return None
        while first and B:
            B -= 1
            first = first.next
        temp = ListNode(None)
        temp.next = A
        second = temp
        while first:
            first = first.next
            second = second.next
        if second and second.next:
            second.next = second.next.next
        return temp.next
        