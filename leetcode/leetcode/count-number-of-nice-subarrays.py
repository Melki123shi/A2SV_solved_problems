class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        result = 0
        curr_count = 0
    

        for r in range(len(nums)):
            if nums[r]%2 != 0:
                curr_count += 1
                count = 0
            if curr_count == k:
                while l < len(nums) and nums[l] % 2 ==0:
                    count+=1
                    l += 1
                count += 1
                curr_count -= 1
                l += 1
            result += count
        return result
            
