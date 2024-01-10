class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
        twos = len(nums) - (ones + zeros)
        nums[:zeros] = [0 for _ in range(zeros)]
        nums[zeros:zeros + ones] = [1 for _ in range(ones)]
        nums[zeros + ones:] = [2 for _ in range(twos)]

        