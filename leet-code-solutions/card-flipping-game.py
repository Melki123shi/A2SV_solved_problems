class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        duplicate = set()
        res = float('inf')
        l = len(fronts)
        for i in range(l):
            if fronts[i] == backs[i]:
                duplicate.add(fronts[i])
        for i in range(l):
            if fronts[i] not in duplicate:
                res = min(res, fronts[i])
            if backs[i] not in duplicate:
                res = min(res, backs[i])
        if type(res) == float:
            return 0
        return res