class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left = 1
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < nums[mid - 1]:
                return nums[mid] 
            if nums[mid] < minimum:
                minimum = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return minimum

        