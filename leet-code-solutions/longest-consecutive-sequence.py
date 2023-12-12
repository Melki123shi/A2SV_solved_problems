class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(len(nums))

        ind = defaultdict(int)
        for i,num in enumerate(nums):
            if num in ind:
                continue
            ind[num] = i

            if num - 1 in ind:
                uf.union(i, ind[num - 1])
            if num + 1 in ind:
                uf.union(i, ind[num + 1])
        return max(uf.size + [0])


class UnionFind:
    def __init__(self, size):
        self.size = [1 for _ in range(size)]
        self.parent = [i for i in range(size)]

    def find(self, x:int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x:int, y:int):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
              

