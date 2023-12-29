class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        nums_t = list(set(nums))
        nums_t.sort()
        temp = nums_t.pop()
        result = 0 

        i = len(nums) - 1
        l = len(nums)
        while i > -1:
            while i > -1 and nums[i] == temp:
                i -= 1
            if nums_t:
                result += (l - i - 1)
                temp = nums_t.pop()
            else:
                break
            if nums_t and nums[i] == nums_t[0]:
                break
        return result
            

