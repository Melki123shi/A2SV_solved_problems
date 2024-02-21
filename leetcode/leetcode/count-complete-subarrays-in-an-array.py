class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        set_nums = set(nums)
        increased = False
        left = 0
        result = 0
        incr = 1
        for right in range(len(nums)):
            while set(nums[left: right + 1]) == set_nums:
                increased = True
                left += 1
                incr += 1
                # print(left, right, incr, result)

            if increased:
                left -= 1
                increased = False
                incr -= 1
                result += incr

        return result
        

            
            
