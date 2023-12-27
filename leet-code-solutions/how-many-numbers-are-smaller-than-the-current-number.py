class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        result = []
        for num in nums:
            result.append(s.index(num))
        return result