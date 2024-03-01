# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderTraversal(root):
            nonlocal k
            if not root:
                return 
            
            result = inOrderTraversal(root.left)
            if result or result == 0:
                return result

            k -= 1
            if k == 0:
                return root.val

            return inOrderTraversal(root.right)
            
        return inOrderTraversal(root)