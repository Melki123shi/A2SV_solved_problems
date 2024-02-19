class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result = 0
        if not maxDoubles:
            return target - 1
        
        if target < 2:
            return 0

        while maxDoubles and target > 1:
            if target % 2 == 0:
                maxDoubles -= 1
                target //= 2
            else:
                target -= 1
            result += 1

        return result + target - 1
