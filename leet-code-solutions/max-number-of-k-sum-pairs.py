class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1
        result = 0
        while i < j:
            sums = nums[i] + nums[j]
            if sums == k:
                i += 1
                j -= 1
                result += 1
            elif sums < k:
                i += 1
            else:
                j -= 1
        return result
        