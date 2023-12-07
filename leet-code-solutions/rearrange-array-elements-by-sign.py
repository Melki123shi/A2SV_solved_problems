class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        negative_pointer = 0
        positive_pointer = 0
        ind = 0

        while ind < len(nums) - 1:
            while nums[positive_pointer] < 0:
                positive_pointer += 1
            while nums[negative_pointer] > 0:
                negative_pointer += 1
            result.append(nums[positive_pointer])
            result.append(nums[negative_pointer])
            positive_pointer += 1
            negative_pointer += 1
            ind += 2
        return result


