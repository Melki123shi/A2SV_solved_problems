class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result = 0
        LENGTH = len(nums)

        
        prefix_sum = 0
        ptr = 0

        while prefix_sum < n:
            if ptr < LENGTH and prefix_sum  + 1 >= nums[ptr]:
                prefix_sum += nums[ptr]
                ptr += 1
            
            else:
                result += 1
                prefix_sum += (prefix_sum + 1)

        return result



        