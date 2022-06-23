# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, node):
        prev = None
        curr = node
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        return prev

    def reorderList(self, A):
        n = 0
        curr = A
        while curr:
            n += 1
            curr = curr.next
        n = n//2
        l = n
        curr = A
        while n > 1:
            curr = curr.next
            n -= 1
        half = curr.next
        curr.next = None
        half = self.reverseList(half)
        curr = A

        while l > 0:
            if curr.next:
                curr.next, half.next, curr, half = half, curr.next, curr.next, half.next
            else:
                curr.next = half
            l -= 1

        return A
        