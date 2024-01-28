class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        res = 0
        total = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] in unique:
                # print(total, l, r, nums[r])
                while l < r and nums[l] != nums[r]:
                    total -= nums[l]
                    unique.remove(nums[l])
                    l += 1
                l += 1
            else:
                unique.add(nums[r])
                total += nums[r]
            res = max(res, total)
        
        return res