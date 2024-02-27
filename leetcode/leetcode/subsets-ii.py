class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        s_set = Counter(nums)

        def backtracking(current_index):
            value = path.copy()
            value.sort()
            if value not in result:
                result.append(value)

            for index in range(current_index + 1, len(nums)):
                candidate = nums[index]
                if s_set[candidate] > 0:
                    path.append(nums[index])
                    s_set[candidate] -= 1

                    backtracking(current_index + 1)
                    s_set[candidate] += 1
                    
                    path.pop()
    
        backtracking(-1)
        result = sorted(result, key=lambda x : x[0] if x else 0)
        return result