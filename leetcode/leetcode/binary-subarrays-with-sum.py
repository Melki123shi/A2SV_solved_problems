class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash_sum = defaultdict(lambda : 0)
        hash_sum[0] += 1
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            difference = prefix_sum - goal
            if difference in hash_sum:
                result += hash_sum[difference]
            hash_sum[prefix_sum] += 1
        return result