class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        self.total = 0

        def recursion():
            if self.total > target:
                return

            elif self.total == target:
                new_path = sorted(path)
                if new_path in result:
                    return
                return result.append(new_path)
                
            for candidate in candidates:
                path.append(candidate)
                self.total += candidate

                recursion()

                self.total -= path[-1]
                path.pop()
        
        recursion()
        return result