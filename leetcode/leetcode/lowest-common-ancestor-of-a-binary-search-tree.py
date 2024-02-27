# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = root

        def helperFunction(root):
            #Base case
            if not root:
                return

            # Recurence relation
            if root.val == p.val or root.val == q.val:
                return self.ancestor

            if root.val < p.val and root.val < q.val:
                self.ancestor = root.right 
                helperFunction(self.ancestor)

            if root.val > p.val and root.val > q.val:
                self.ancestor = root.left 
                helperFunction(self.ancestor)

            return self.ancestor

        return helperFunction(self.ancestor)

            
