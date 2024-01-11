class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        m = (float('inf'))
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                m = min(m, r - l + 1)
                total -= nums[l]
                l += 1
        if type(m) == float:
            return 0
        return m
