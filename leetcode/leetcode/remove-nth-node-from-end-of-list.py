# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        head = dummy

        size = head
        for i in range(n - 1):
            size = size.next

        current = head
        prev = current
        while size.next:
            prev = current
            current = current.next
            size = size.next
        prev.next = current.next

        return head.next

        

        

