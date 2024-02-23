# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], maximum = float('inf'), minimum = float('-inf')) -> bool:
        if not root:
            return True

        print(minimum, maximum, root.val)
        if minimum >= root.val  or maximum <= root.val:
            return False
        
        return self.isValidBST(root.right, minimum = root.val, maximum = maximum) and self.isValidBST(root.left, maximum = root.val, minimum = minimum)
        
       

