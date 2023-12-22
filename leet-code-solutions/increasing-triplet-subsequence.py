class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        i = 0
        j = 1
        k = 2

        while k < len(nums):
            if nums[k] > nums[j] > nums[i]:
                return True
            if nums[i] >= nums[j]:
                i += 1
                j += 1
            elif nums[k] < nums[i]:
                i = k
            elif nums[k] > nums[i]:
                j = k
            k += 1
        return False

            
        