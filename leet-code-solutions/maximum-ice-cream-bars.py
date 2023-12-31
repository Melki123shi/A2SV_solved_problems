class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c = [0 for _ in range(max(costs) + 1)]
        total = 0
        count = 0

        for cst in costs:
            c[cst] += 1

        for i,cst in enumerate(c):
            if total == coins:
                return count
            else:
                while cst != 0:
                    if total + cst*i > coins:
                        cst -= 1
                    else:
                        total += cst*i
                        count += cst
                        break
        return count
        

        