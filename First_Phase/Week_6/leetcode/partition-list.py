# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        temp1 = dummy
        
        temp2 = ListNode()
        temp2.next = head
        temp = temp2
        
        while temp and temp.next:
            if temp.next.val < x:
                temp1.next = temp.next
                temp1 = temp1.next
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        temp.next = None
        temp1.next = temp2.next
        
        return dummy.next
