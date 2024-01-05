class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        res = 0
        size = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in unique:
                size += 1
            else:
                temp = s[right]
                while s[left] != temp:
                    unique.remove(s[left])
                    left += 1
                left += 1
                size = right - left + 1

            unique.add(s[right])
            res = max(res, size)
            # print(unique, res)
        
        return res

        