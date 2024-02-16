class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = Counter(s)
        length = 0
        odd = False
        for key in s:
            if s[key] % 2 == 0:
                length += s[key]
            else:
                length += s[key] - 1
                odd = True   

        return length + 1 if odd else length
            