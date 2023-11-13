class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True]*n
        is_prime[0] , is_prime[1] = False, False

        num = ceil(sqrt(n))
        for i in range(2, num):
            for j in range(i*i, n, i):
                is_prime[j] = False
        count = Counter(is_prime)
        return count[True]
