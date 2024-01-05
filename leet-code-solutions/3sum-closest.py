class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = float('inf')
        res = total
        for i in range(len(nums)-2):
            right = len(nums) - 1
            left = i + 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                if abs(total - target) < abs(res - target):
                    res = total
                if total < target:
                    left += 1
                else:
                    right -= 1 
        return res


