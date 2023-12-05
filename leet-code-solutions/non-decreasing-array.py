class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        out_of_order = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if out_of_order == 1 or ((i > 0) and (i + 2 < len(nums)) and (nums[i + 1] < nums[i - 1]) and (nums[i] > nums[i + 2])):
                    return False
                out_of_order += 1
        return True