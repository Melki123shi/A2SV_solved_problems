class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        total = 0
        prefix_sum = [0]*len(nums)
        ans = []
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1] 
        prefix_sum.append(prefix_sum[-1] + nums[-1])
        for q in queries:
            if q >= prefix_sum[-1]:
                ans.append(len(nums))
            else:
                i = 0
                j = len(prefix_sum) 

                while i < j:
                    m = (i + j) // 2
                    if prefix_sum[m] == q or (prefix_sum[m] < q < prefix_sum[m + 1]):
                        ans.append(m )
                        break
                    if prefix_sum[m] < q:
                        i = m + 1
                    else:
                        j = m 
        return ans
                    
