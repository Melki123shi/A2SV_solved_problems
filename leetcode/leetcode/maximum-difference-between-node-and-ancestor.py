# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(root, maximum = root.val, minimum = root.val):
            if not root:
                return self.result
            
            maximum = max(maximum, root.val)
            minimum = min(minimum, root.val)
            
            self.result = max(self.result, maximum - minimum)

            dfs(root.right, maximum = maximum, minimum = minimum)
            dfs(root.left, maximum = maximum, minimum = minimum)

            return self.result

        return dfs(root)

        
        


        

        