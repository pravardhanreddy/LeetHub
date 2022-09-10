# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            prev = ListNode(None)
            head = prev
            curr1 = list1
            curr2 = list2
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    prev.next, curr1 = curr1, curr1.next
                else:
                    prev.next, curr2 = curr2, curr2.next
                prev = prev.next
            prev.next = curr1 if curr1 else curr2
            return head.next
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(merge(l1, l2))
            lists = merged
        return lists[0] if lists else None