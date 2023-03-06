class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashT1 = {}
        hashT2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashT1:
                hashT1[s[i]] = t[i]
                print(hashT1)
            elif (s[i] in hashT1) and ((hashT1[s[i]] != t[i])):
                return False
        for i in range(len(s)):
            if t[i] not in hashT2:
                hashT2[t[i]] = s[i]
                print(hashT2)
            elif (t[i] in hashT2) and ((hashT2[t[i]] != s[i])):
                return False
        else:
            return True
