class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p1 = []
        p2 = []
        p = 1
        l = len(nums)
        for i in range(l):
            p*=nums[i]
            p1.append(p)
        p = 1
        for i in range(l-1,-1,-1):
            p*=nums[i]
            p2.append(p)
        for i in range(l):
            if i == 0:
                nums[i] = p2[-2]
            elif i == l-1:
                nums[i] = p1[-2]
            else:
                nums[i] = p1[i - 1] * p2[l - 2-i]
                
        return nums