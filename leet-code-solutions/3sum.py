class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total = defaultdict()
        l = len(nums)
        uniq = set()
        result = []
        for i in range(l):
            for j in range(i + 1, len(nums)):
                if -1*(nums[i] + nums[j]) in total:
                    comb = [-1*(nums[i] + nums[j]), nums[i], nums[j]]
                    comb.sort()
                    comb = tuple(comb)
                    # print(comb)
                    if  comb not in uniq:
                        result.append([-1*(nums[i] + nums[j]), nums[i], nums[j]])
                    uniq.add(comb)
            total[nums[i]] = i
        return result
        