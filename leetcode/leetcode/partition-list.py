# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Defining variables
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        less = []
        found = False

        # Find elements less than x and store them in list and remove them
        curr = head.next
        prev = head
        while curr:
            if not found and curr.val >= x:
                found = True
                prev = curr
                curr = curr.next
                continue

            if found and curr.val < x:
                less.append(curr)
                prev.next = curr.next
                curr = prev
            prev = curr
            curr = curr.next

        # find the first elemnt greater or equal to x and put the lees than elements before it 
        curr = head.next
        prev = head
        i = 0
        while curr and curr.val < x:
            prev = curr
            curr = curr.next

        for l in less:
            curr = head.next
            i =0 
            l.next = prev.next
            prev.next = l
            prev = l

        return head.next