# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(list1, list2, list3 = ListNode()):
            if not list1 and not list2:
                return None
            
            if not list1 and list2:
                list3.next = list2
                list2 = list2.next
            elif not list2 and list1:
                list3.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

            recursion(list1, list2, list3)
            return list3
        
        result = recursion(list1, list2)
        return result

    

                    
