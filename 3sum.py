class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i,v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            
            p1 = i+1
            p2 = len(nums)-1

            while p1 < p2:
                s = nums[p1]+nums[p2]+v
                if s == 0:
                    ans.append([nums[p1],nums[p2],v])
                    p1+=1
                    while nums[p1] == nums[p1-1] and p1 < p2:
                        p1+=1
                elif s > 0:
                    p2-=1
                else:
                    p1+=1
        return ans
            

                    
