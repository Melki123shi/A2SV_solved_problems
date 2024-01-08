class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        i = j = 0
        k = 1

        while  j < len(nums):
            if nums[j] == 0:
                k-=1 
            if k < 0:
                if nums[i] == 0:
                    k+=1
                i+=1
            j+=1
        return j - i - 1