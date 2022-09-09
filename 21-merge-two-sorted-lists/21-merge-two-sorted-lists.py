# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        curr1 = list1
        curr2 = list2
        
        head = ListNode(None)
        curr = head
        
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr1, curr.next = curr1.next, curr1
            else:
                curr2, curr.next = curr2.next, curr2
            curr = curr.next
            
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
        
        return head.next