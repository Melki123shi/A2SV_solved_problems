class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = len(s) - 1
        j = len(g) - 1
        result = 0
        while i > -1 and  j > -1:
            if g[j] <= s[i]:
                result += 1
                i -= 1
            j -= 1
        return result

                                                