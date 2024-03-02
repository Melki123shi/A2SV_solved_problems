# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MinMax:
    def __init__(self):
        self.min = float('inf')
        self.max = float('-inf')
        self.isBST = True
        self.max_sum = 0
        self.total_sum = 0

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return MinMax()

            left = dfs(root.left)
            right = dfs(root.right)

            newMiniMax = MinMax()

            if (not left.isBST or not right.isBST or left.max >= root.val or right.min <= root.val):
                newMiniMax.isBST = False
                newMiniMax.max_sum = max(left.max_sum, right.max_sum)
                
            else:
                newMiniMax.isBST = True
                newMiniMax.total_sum = left.total_sum + right.total_sum + root.val
                newMiniMax.max_sum = max(newMiniMax.total_sum, left.max_sum, right.max_sum)

                newMiniMax.min = left.min if root.left else root.val
                newMiniMax.max = right.max if root.right else root.val
            
            return newMiniMax
            
        result = dfs(root).max_sum
        if result < 0:
            return 0 
        return result


       

        



