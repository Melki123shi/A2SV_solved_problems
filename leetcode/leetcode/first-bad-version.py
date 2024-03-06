# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 0, n
        while i <= j:
            m = (i + j) // 2
            if isBadVersion(m) == True:
                if isBadVersion(m - 1) == False:
                    return m 
                else:
                    j = m - 1
            else:
                i = m + 1