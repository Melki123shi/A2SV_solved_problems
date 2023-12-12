class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        while len(str(n)) > 1 or n % 2 != 0:
            nums = [int(x)**2 for x in str(n)]
            total = sum(nums)
            if total == 1:
                return True
            n = total
        return False
