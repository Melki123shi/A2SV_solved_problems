class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        store = {}
        for i in nums:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1

        j = 0
        if 0 in store:
            for i in range(store[0]):
                nums[j] = 0
                j+=1
        if 1 in store:
            for i in range(store[1]):
                nums[j] = 1
                j+=1
                
        if 2 in store:
            for i in range(store[2]):
                nums[j] = 2
                j+=1
        
