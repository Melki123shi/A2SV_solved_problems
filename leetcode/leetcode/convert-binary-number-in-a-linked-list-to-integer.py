# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        size = 0
        numbers = []
        current = head
        while current:
            numbers.append(current.val)
            current = current.next
            size += 1
        
        result = 0
        for i, number in enumerate(numbers):
            result += ((2**(size - i - 1)) * number)
        
        return result