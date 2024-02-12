# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        def compute_size(head):
            current = head
            size = 0
            while current:
                current = current.next
                size += 1
            return size
        
        head = dummy
        size = compute_size(dummy) - 1
        ind = size - n + 1
        current = head
        prev = current
        while current.next and ind:
            prev = current
            current = current.next
            ind -= 1
        prev.next = current.next

        return head.next

        

        

