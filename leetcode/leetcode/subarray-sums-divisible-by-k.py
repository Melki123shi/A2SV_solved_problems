class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hash_sum = defaultdict(lambda : 0)
        hash_sum[0] += 1
        result = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in hash_sum:
                result += hash_sum[remainder]
            hash_sum[remainder] += 1
        
        return result
        