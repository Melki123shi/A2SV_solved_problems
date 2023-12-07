class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l1, l2 = [], []
        for match in matches:
            l1.append(match[0])
            l2.append(match[1])
        l1 = set(l1)
        l2 = Counter(l2)

        res = []
        for key in l2:
            if key in l1:
                l1.remove(key)
            if l2[key] < 2:
                res.append(key)
        res.sort()
        l1 = list(l1)
        l1.sort()
        return [l1, res]
