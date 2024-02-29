# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dict = defaultdict(list)
        def traverse(root, level = 0):
            if not root:
                return

            # print(self.dict, level, root.val)

            if level % 2 == 0:
                self.dict[level].append(root.val)
            else:
                self.dict[level].insert(0, root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
                # traverse(root.left, level + 1)
                # traverse(root.right, level + 1)

        traverse(root)
        return [x for x in self.dict.values()]





        
        

        
        
        