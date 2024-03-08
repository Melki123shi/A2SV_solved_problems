# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n 

        while left <= right:
            mid = (left + right) // 2

            if (mid == 1 and isBadVersion(mid)== True): return 1
            if (mid != 1 and isBadVersion(mid)== True and isBadVersion(mid - 1) == False): return mid
            if (mid != n and isBadVersion(mid + 1) == True and isBadVersion(mid)== False): return mid + 1
            if isBadVersion(mid)== False:
                left = mid
            else:
                right = mid - 1

        