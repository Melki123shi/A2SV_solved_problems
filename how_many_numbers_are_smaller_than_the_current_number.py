class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        unsorted = []
        ans = []
        for i in nums:
            unsorted.append(i)
        nums.sort()
        for i in unsorted:
            j = 0
            count = 0
            while i != nums[j]:
                count+=1
                j+=1
            ans.append(count)
            
        return ans
