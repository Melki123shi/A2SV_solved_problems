class Solution:
    def largestOddNumber(self, num: str) -> str:
        while int(num[-1]) % 2 == 0:
            num = num[:-1]
            if num == '':
                return ""
        return num