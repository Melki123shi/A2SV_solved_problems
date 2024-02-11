class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum = 0
        total_sum = sum(nums)
        ans = []
        for i, num in enumerate(nums):
            right_sum = total_sum - num - left_sum

            left_size, right_size = i, len(nums) - i - 1
            ans.append(
                left_size*num - left_sum - right_size*num + right_sum
            )

            left_sum += num
        
        return ans