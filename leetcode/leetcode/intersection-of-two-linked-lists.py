# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first, second = headA, headB
        size1 = size2 = 0

        while first:
            size1 += 1
            first = first.next
        
        while second:
            size2 += 1
            second = second.next
        

        first, second = headA, headB
        diff = abs(size1 - size2)
        
        if size1 > size2:
            for i in range(diff):
                first = first.next
        else:
            for i in range(diff):
                second = second.next
        
        while first and second:
            if first == second:
                return first
            first = first.next
            second = second.next
        
            
        
