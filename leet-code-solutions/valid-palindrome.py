class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        s = s.lower()
        for st in s:
            if 96 < ord(st) < 123 or 47 < ord(st) < 58:
                result += st
        return result == result[::-1]