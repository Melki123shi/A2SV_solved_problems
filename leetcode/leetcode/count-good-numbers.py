class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = int(10**9 + 7)
        def power(num, p, MOD):
            if p <= 0:
                return 1
            
            if p % 2 == 0:
                return power((num * num) % MOD, p // 2 , MOD)
                
            return num * power((num * num) % MOD, (p - 1) // 2 , MOD)


        if n == 1:
            return 5

        val = power(20, n//2, MOD)

        if n % 2 == 0:
            result = val
        else:
            result = val * 5
        
    
        return result % MOD

        
        