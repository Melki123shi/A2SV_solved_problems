# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head

        start = head
        prev = None
        while left != 1:
            prev = start
            start = start.next
            left -= 1

        end = head
        while right != 1:
            end = end.next
            right -= 1

        pointer = start.next
        if prev:
            prev.next = end
        else:
            head = end
        start.next = end.next

        prev = start
        start = pointer
        pointer = pointer.next
        while prev != end:
            start.next = prev
            prev = start
            start = pointer
            if not pointer:
                break
            pointer = pointer.next

        return head


        




        