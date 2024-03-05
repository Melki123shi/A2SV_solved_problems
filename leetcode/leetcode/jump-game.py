class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        goal_pos = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal_pos:
                goal_pos = i
        
        return goal_pos == 0