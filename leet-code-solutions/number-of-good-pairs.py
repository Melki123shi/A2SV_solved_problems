class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dup = Counter(nums)
        c= 0

        for n in dup:
            c += sum(range(dup[n]))
        return c
        