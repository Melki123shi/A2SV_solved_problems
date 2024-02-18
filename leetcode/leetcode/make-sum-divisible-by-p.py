class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        result = 0
        remender = sum(nums) % p
        if remender == 0:
            return 0
        
        prefix_sum = 0
        mod = defaultdict()
        mod[0] = -1
        n = len(nums)
        result = n
        for i, num in enumerate(nums):
            prefix_sum += num
            key = prefix_sum % p - remender
            if key < 0:
                key += p
            if key in mod:
                result = min(result, i-mod[key])
            mod[prefix_sum % p] = i

        return result if result < n else -1