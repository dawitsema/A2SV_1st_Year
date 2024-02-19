# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
            
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        
        rev_list = nodes[left-1:right][::-1]
        
        new_head = ListNode(nodes[0])
        curr = new_head
        for i in range(1, len(nodes)):
            new_node = ListNode(nodes[i])
            curr.next = new_node
            curr = curr.next
        
        nodes[left-1:right] = rev_list
        curr = head
        for i in range(len(nodes)):
            curr.val = nodes[i]
            curr = curr.next
        
        return head