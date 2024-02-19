# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        for x in range(n):
            second = second.next
        while second:
            nex = first.next
            second = second.next
            if second is None:
                first.next = nex.next
                break
            else: first = first.next
        else:
            if n == 1: head = None
            else: head = head.next
        return head