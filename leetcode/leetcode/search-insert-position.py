class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        while left < right:
            mid = (left + right) // 2
            if mid != 0 and nums[mid - 1] < target and nums[mid] >= target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 

            