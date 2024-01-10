class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        s1_d = Counter(s1)
        for r in range(len(s1) - 1, len(s2)):
            s2_d = Counter(s2[l : r + 1])
            if s2_d == s1_d:
                return True
            l += 1
        return False


        