class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        c = Counter(nums)
        res = 0
        keys = list(c.keys())
        # print(type(keys))
        for i in range(len(keys) - 1):
            if abs(keys[i] - keys[i + 1]) == 1:
                res = max(res, c[keys[i]] + c[keys[i] + 1])

        return res

            

