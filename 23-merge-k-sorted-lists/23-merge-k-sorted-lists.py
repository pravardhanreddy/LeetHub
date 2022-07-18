# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import merge

def travel(node): # Convert linked list to list
    root = node
    while root:
        yield root.val
        root = root.next

def getLinkedList(node): # Convert list to linked list
    temp = ListNode(None)
    head = temp
    for i in range(len(node)):
        temp.next = ListNode(node[i])
        temp = temp.next
    return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        iterables = [list(travel(x)) for x in lists]
        ans = list(merge(*iterables))
        return getLinkedList(ans)