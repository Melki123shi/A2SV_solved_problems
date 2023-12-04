class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        m = 0
        for i in s:
            m = max(len(i), m)
        
        for i in range(len(s)):
            s[i] = s[i] + ' '*(m - len(s[i]))

        d = {}
        j = 0
        i = 0
        while i < len(s) and j < len(s[0]):
            d[j] = s[i][j]
            j += 1
        
        for i in range(1, len(s)):
            j = 0
            while j < len(s[0]):
                d[j] = d[j] + s[i][j]
                j += 1
        ans = [x.rstrip() for x in d.values()]
        return ans
