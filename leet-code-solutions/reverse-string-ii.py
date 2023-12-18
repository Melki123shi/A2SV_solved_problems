class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        while i < len(s):
            temp = s[i : i + k]
            temp = temp[::-1]
            if i == 0:
                s = temp + s[i + k: ]
            else:
                s = s[ : i] + temp + s[i + k : ]
            i += 2 * k
        return s
        