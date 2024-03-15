class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isValid(minSum):
            current = 0
            divider = 1
            for num in nums:
                current += num
                if current > minSum:
                    divider += 1
                    current = num
    
            return divider

        mini = max(nums)
        maxi = sum(nums)
        while mini <= maxi:
            mid = mini + (maxi - mini)//2
            result = isValid(mid)
            if result <= k:
                maxi = mid - 1
            else:
                mini = mid + 1

        return (mini)