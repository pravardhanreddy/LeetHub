# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        curr = head
        store = head.next
        curr.next = None
        while store:
            temp = store.next
            store.next = curr
            curr = store
            store = temp
        return curr