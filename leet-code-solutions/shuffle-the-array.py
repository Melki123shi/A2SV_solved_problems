class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n 

        while i < j < len(nums):
            nums.insert(i+1,nums.pop(j))
            i += 2
            j += 1
        return nums