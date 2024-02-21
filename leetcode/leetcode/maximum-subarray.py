class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        l = 0
        total = nums[0]
        res = total
        for r in range(1,len(nums)):
            total += nums[r]
            if nums[r] >= 0:
                while total < nums[r] and l <= r:
                    total -= nums[l]
                    l += 1
            res = max(res,total)
        
        return res
