# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        pointer = head.next
        prev = None
        while pointer:
            current.next = prev
            prev = current
            current = pointer
            pointer = pointer.next
        current.next = prev
        return current

        
        