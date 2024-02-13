# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        tail = head
        size = 0
        while tail.next:
            tail = tail.next
            size += 1
        
        ptr = 1
        current = head
        prev = None
        while current and ptr <= size+1:
            # print(tail.val)
            if ptr % 2 == 0:
                temp = current
                tail.next = temp
                prev.next = current.next
                temp.next = None
                tail = temp
                current = prev             
            prev = current
            current = current.next
            ptr += 1
        return head
        