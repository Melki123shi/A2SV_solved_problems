# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)    
        elif low > root.val:
            return self.rangeSumBST(root.right, low, high)
        elif high < root.val:
            return self.rangeSumBST(root.left, low, high)


        
        
