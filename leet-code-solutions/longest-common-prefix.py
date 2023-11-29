class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        
        start = strs[0]
        m = len(strs[0])
        for i,s in enumerate(strs):
            m = min(m, len(s))
            for j in range(len(s)-1, -1, -1):
                if j >= len(start):
                    continue
                if start[j] != s[j]:
                    start = start[:j]
        return start[:m]
                