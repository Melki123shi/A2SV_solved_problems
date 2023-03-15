class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2= len(nums)-1
        c=0
        
        while p1<= p2:
            if nums[p1] != val:
                p1+=1
            elif nums[p1] == val and nums[p2]!= val:
                nums[p1] = nums[p2]
                c+=1
                p1+=1
                p2-=1
            elif nums[p2]== val:
                p2-=1
                c+=1
            elif nums[p1] != val and nums[p2]!=val:
                p1+=1
                p2-=1
        return len(nums)-c
