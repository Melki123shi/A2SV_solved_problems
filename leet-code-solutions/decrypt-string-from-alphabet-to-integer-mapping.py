class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                ans += chr((int(s[i - 2] + s[i - 1]) + 96))
                i -= 3
            else:
                ans += chr((int(s[i]) + 96))
                i -= 1
        ans = ans[::-1]
        return ans
            




            
            