class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        unique = {}
        res = 0

        for r in range(len(s)):
            char = s[r]
            if char in unique and unique[char] >= l:
                l = unique[char] + 1
            res = max(res, (r - l + 1))
            unique[char] = r
        return res
                