class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        orig = x
        dig = 0
        while x != 0:
            dig *= 10
            dig += (x % 10)
            x = x // 10
        return dig == orig
