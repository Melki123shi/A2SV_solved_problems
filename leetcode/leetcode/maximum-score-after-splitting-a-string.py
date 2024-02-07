class Solution:
    def maxScore(self, s: str) -> int:
        total = sum([int(x) for x in s])
        res = 0
        for r in range(len(s) - 1):
            if s[r] == '1':
                total -= 1
            else:
                total += 1
            res = max(res, total)
        return res

        