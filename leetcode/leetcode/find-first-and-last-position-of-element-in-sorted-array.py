class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = float('inf')
        end = float('inf')

        if len(nums) == 0:
            return [-1, -1]

        if nums[0] == target:
            start = 0
        
        else:
            l = 1
            r = len(nums) - 1
            while l <= r:
                mid = (l + r)//2
                if nums[mid - 1] != target and nums[mid] == target:
                    start = mid
                    break
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        if nums[len(nums) - 1] == target:
            end = len(nums) - 1
        else:
            l = 0
            r = len(nums) - 2

            while l <= r:
                mid = (l + r)//2
                if nums[mid + 1] != target and nums[mid] == target:
                    end = mid
                    break
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
        if type(start) == float or type(end) == float:
            return [-1,-1]
        return [start,end]
        