class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0

        for i in range(len(nums)):
            right -= nums[i]
            if right == left:
                return i
            left += nums[i]
        return -1




        