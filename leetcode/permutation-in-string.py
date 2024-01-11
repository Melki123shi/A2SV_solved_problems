class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        
        s1_d = [0]*26
        for s in s1:
            s1_d[ord(s) - 97] += 1
       
        for l in range(len(s2)):
            s2_d = [0]*26
            r = l + len(s1)
            
            for k in s2[l: r]:
                s2_d[ord(k) - 97] += 1

            if s2_d == s1_d:
                return True
        return False


        