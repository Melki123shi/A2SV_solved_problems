# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.max = 0
        self.result = []
        self.counter = 1


        def recursion(root):
            if not root:
               return

            recursion(root.left)
            
            if self.prev == root.val:
                self.counter += 1
            else:
                self.counter = 1
                self.prev = root.val

            if self.counter > self.max:
                self.max = self.counter
                self.result = [root.val]
            elif self.counter == self.max:
                self.result.append(root.val)
            
            recursion(root.right)
        
        recursion(root)
        return self.result


        