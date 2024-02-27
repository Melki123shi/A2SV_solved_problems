# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root1, root2 = root.left, root.right

        def helperFunction(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False 
            
            if root1.val != root2.val:
                return False
            
            return helperFunction(root1.left, root2.right) and helperFunction(root2.left, root1.right)

        return helperFunction(root1, root2)
        