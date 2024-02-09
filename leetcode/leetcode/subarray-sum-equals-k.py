class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_sum = {0:1}
        prefix_sum = 0
        result = 0

        for ind, num in enumerate(nums):
            prefix_sum += num
            difference = prefix_sum - k
            if difference in hash_sum:
                result += hash_sum[difference]
            if prefix_sum not in hash_sum:
                hash_sum[prefix_sum] = 1
            else:
                hash_sum[prefix_sum] += 1
        return result



