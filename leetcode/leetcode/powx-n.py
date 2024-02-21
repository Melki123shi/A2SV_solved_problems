class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if x == 0:
            return 0

        if n < 0: 
            n = abs(n)
            if n % 2 == 0:
                return 1/(self.myPow(x*x, n//2)
)
            return 1/(x * self.myPow((x*x), (n - 1)// 2))

        if n % 2 == 0:
            return self.myPow(x*x, n//2)

        return x * self.myPow(x*x, (n - 1)// 2)
