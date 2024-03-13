class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x // 2

        if x < 2:
            return x

        while i <= j:
            mid = (i + j) // 2
            if mid ** 2 == x:
                return mid
            
            if mid ** 2 > x and (mid - 1) ** 2 < x:
                return mid - 1

            if mid ** 2 < x:
                i = mid + 1
            elif mid ** 2 > x:
                j = mid  - 1

        return mid 
