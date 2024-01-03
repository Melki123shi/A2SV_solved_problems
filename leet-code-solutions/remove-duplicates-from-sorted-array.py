class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0

        while i < len(nums) and j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        return len(nums[:i + 1])
                
                
        
        