# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def rotateRight(self, A, B):
		if not A or not A.next:
			return A
		n = 0
		curr = A
		while curr:
			curr = curr.next
			n += 1
		B = B%n
		if B == 0:
			return A
		first, second = A, A
		for i in range(B):
			first = first.next
		while first and first.next:
			first = first.next
			second = second.next
			
		first.next, second.next, head = A, None, second.next
		return head
        