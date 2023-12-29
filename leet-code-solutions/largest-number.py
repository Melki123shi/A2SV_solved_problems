class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            j = i
            while j > 0 and str(nums[j]) + str(nums[j - 1]) > str(nums[j - 1]) + str(nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
        return str(int(''.join([str(x) for x in nums])))

