class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        s_set = set()
        
        def backtracking(num):
            if len(path) == len(nums):
                result.append(path.copy())

            s_set = set(path)

            for candidate in nums:
                if candidate not in s_set:
                    path.append(candidate)

                    backtracking(candidate)

                    path.pop()
        
        backtracking(nums)
        return result