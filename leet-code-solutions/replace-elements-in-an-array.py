class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = defaultdict()
        for i, num in enumerate(nums):
            dic[num] = i
        for op in operations:
            if op[0] in dic:
                dic[op[1]] = dic[op[0]]
                del dic[op[0]]
        dic = dict(sorted(dic.items(), key=lambda x: x[1]))
        return dic
