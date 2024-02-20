# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.dummy = ListNode(-5001)

        while head:
            temp, head = head, head.next
            temp.next = None

            curr = self.dummy
            while curr and curr.val < temp.val:
                prev = curr
                curr = curr.next
            
            temp.next, prev.next = prev.next, temp

        return self.dummy.next


