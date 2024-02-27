# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], num = 0) -> int:
        if not root:
            return 0

        num = num * 10 + root.val
        if not root.right and not root.left:
            return num

        return self.sumNumbers(root.right, num) + self.sumNumbers(root.left, num)

            



        