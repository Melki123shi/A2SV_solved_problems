class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        s = 0
        e = x/2+1
        ans = 0
        
        while s < e:
            mid = (s+e)/2
            if ans == mid:
                return int(ans)
            if mid**2 == x:
                ans = mid
                return int(ans)
            elif mid ** 2 < x:
                ans = mid
                s = mid
            elif mid **2 > x:
                ans = mid
                e = mid
        return int(mid)
        
