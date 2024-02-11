class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        
        # compute the prefix sum
        for start, end in requests:
            prefix_sum[start] += 1
            prefix_sum[end + 1] -= 1

        for i in range(1, len(nums) + 1):
            prefix_sum[i] += prefix_sum[i - 1]
        
        prefix_sum.pop()

        nums.sort()
        prefix_sum.sort()

        result = 0
        for i in range(len(nums)):
            result += (nums[i] * prefix_sum[i])
        
        return result % (10**9 + 7)
        
