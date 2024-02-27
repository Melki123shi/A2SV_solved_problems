class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backTraking(num):
            if len(path) == k:
                return ans.append(path.copy())
            
            for candidate in range(num + 1, n + 1):
                path.append(candidate)

                # Backtraking
                backTraking(candidate)

                #remove from path
                path.pop()
            
        
        backTraking(0)
        return ans

                
        