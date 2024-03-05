class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        result = 0

        for i in range(2, len(nums)):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    result += (right - left)
                    right -= 1
                else:
                    left += 1
                
        return result
        

