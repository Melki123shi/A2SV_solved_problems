# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # define a function the length of whole array
        def length(current):
            count = 0
            while current:
                count += 1
                current = current.next
            return count
        
        # conpute a function the length of whole array
        current = head
        LENGTH = length(current)

        # computer the remender and the minimum path length
        remender = LENGTH % k
        path_length = LENGTH // k
    
        result = []
        count = 0
        current = head
        while current:
            count += 1
            nextNode = current.next
            if remender:
                if count == 1 + path_length:
                    remender -= 1
                    result.append(head)
                    head = nextNode
                    current.next = None
                    count = 0
            else:
                if count == path_length:
                    result.append(head)
                    head = nextNode
                    current.next = None
                    count = 0

            current = nextNode

        while len(result) < k:
            result.append(None)
        
        return result
        