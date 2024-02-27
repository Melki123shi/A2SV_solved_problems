class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        s_set = set()

        def backtracking(current_index):
            value = path.copy()
            value.sort()
            if value not in result:
                result.append(value)

            s_set = set(path)
            
            for index in range(current_index + 1, len(nums)):
                candidate = nums[index]
                if candidate not in s_set:
                    path.append(nums[index])

                    backtracking(current_index + 1)

                    path.pop()
        
        backtracking(-1)
        result = sorted(result, key=lambda x : x[0] if x else 0)
        return result
