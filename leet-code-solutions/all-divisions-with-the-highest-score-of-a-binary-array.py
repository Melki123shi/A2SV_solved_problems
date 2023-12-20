class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        result = defaultdict(lambda : [])
        maximum = ones
        result[ones].append(0)
        for left, num in enumerate(nums):
            if num == 0:
                ones += 1
            else:
                ones -= 1
            maximum = max(maximum, ones)
            result[ones].append(left + 1)
        return result[maximum]



        