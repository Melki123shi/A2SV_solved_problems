class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
        res = count
        left = 0
        for right in range(k, len(s)):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            res = max(res, count)
            left += 1
        return res

        