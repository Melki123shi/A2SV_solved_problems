class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        result = 0
        current = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > current:
                spaces = ceil(nums[i]/current)
                current = nums[i]//spaces
                result += spaces - 1
            else:
                current = nums[i]
        
        return result