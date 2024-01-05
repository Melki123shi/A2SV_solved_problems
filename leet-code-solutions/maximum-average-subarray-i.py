class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        total = sum(nums[:right])
        result = total
        while right < len(nums):
            total = total - nums[left] + nums[right]
            result = max(total, result)
            left += 1
            right += 1
        return result/k
