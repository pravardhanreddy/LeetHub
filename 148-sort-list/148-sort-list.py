# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def getMiddle(self, h):
        if not h:
            return h
        fast, slow = h, h
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        result = ListNode(None)
        head = result
        while left and right:
            if left.val <= right.val:
                result.next = left
                left = left.next
            else:
                result.next = right
                right = right.next
            result = result.next
        result.next = left if left else right
        return head.next
                    
    def sortList(self, A):
        if not (A and A.next):
            return A
        m = self.getMiddle(A)
        nxt = m.next
        m.next = None
        left = self.sortList(A)
        right = self.sortList(nxt)
        
        return self.sortedMerge(left, right)
        