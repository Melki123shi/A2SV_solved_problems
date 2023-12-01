class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        m = min(l1, l2)
        ans = ''

        for i in range(m):
            ans += word1[i]
            ans += word2[i]

        if l1 == l2:
            return ans
        if l1 == m:
            ans += word2[i+1:]
        else:
            ans += word1[i+1:]
        return ans