class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 0
        e = num//2
        if num == 1 or num == 0:
            return True
        while s <= e:
            if e**2 == num:
                return True
            mid = (s+e)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                if s == mid:
                    return False
                s = mid
            elif mid**2 > num:
                if e == mid:
                    return False
                e = mid
        return False
