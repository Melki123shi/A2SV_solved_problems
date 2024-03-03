class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.LENGTH = len(candidates)
        path = []
        result = []
        candidates.sort()

        if sum(candidates) < target:
            return

        if sum(candidates) == target:
            return [candidates]

        def backtracking(index, total):
            if total > target:
                return

            if total == target:
                return result.append(path.copy())

            for i in range(index, self.LENGTH):
               
                candidate = candidates[i]
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                if candidate > target:
                    continue

                path.append(candidate)
                backtracking(i + 1, total + candidate)
                path.pop()
        
        backtracking(0, 0)
        return result
        