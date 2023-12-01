class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        res = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i < len(s) - 1 and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    res += d[s[i + 1]] - d[s[i]]
                    i += 2
                else:
                    res +=  d[s[i]]
                    i += 1
            elif s[i] == 'X':
                if i < len(s) - 1 and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    res += d[s[i + 1]] - d[s[i]]
                    i += 2
                else:
                    res +=  d[s[i]]
                    i += 1
            elif s[i] == 'C':
                if i < len(s) - 1 and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    res += d[s[i + 1]] - d[s[i]]
                    i += 2
                else:
                    res +=  d[s[i]]
                    i += 1
            else:
                res +=  d[s[i]]
                i += 1
        return res
            
        