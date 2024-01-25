class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        total = 0
        res = 0
        d = {}
        l = 0
        for r in range(len(fruits)):
            if fruits[r] in d:
                d[fruits[r]] += 1
            else:
                d[fruits[r]] = 1
            total += 1

            while l < r and len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
                total -= 1
            res = max(res, total)
            

            
        return res

            
