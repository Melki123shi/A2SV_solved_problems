class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(index, total):
            nonlocal k,n
            if total > n:
                return

            if len(path) == k:
                if total == n:
                    return result.append(path.copy())
                return
            
            for number in range(index, min(n , 10)):
                path.append(number)
                backtracking(number + 1, total + number)
                path.pop()
        
        backtracking(1,0)
        return result

                
        