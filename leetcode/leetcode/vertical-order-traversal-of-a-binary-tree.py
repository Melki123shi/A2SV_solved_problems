# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = defaultdict(list)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, start = 0, level = 0):
            if not root:
                return start
            self.index[start].append([root.val, level])


            dfs(root.left, start - 1, level + 1)
            dfs(root.right, start + 1, level + 1)

        dfs(root)

        for key in self.index:
            self.index[key] = sorted(self.index[key], key=lambda x : (x[1], x[0]))

        for key in self.index:
            self.index[key] = [x[0] for x in self.index[key]]

        return [x for x in OrderedDict(sorted(self.index.items())).values()]


        