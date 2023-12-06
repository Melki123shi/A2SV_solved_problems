class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = Counter(nums)
        ans = []

        for n in nums:
            if (nums[n] > (l // 3)):
                ans.append(n)
        return ans
