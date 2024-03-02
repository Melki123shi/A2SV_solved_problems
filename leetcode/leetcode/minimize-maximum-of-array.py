class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        result = 0
        for i, num in enumerate(nums):
            prefix_sum += nums[i]
            result = max(result, ceil(prefix_sum / (i + 1)))
        return result