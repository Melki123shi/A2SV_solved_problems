class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        result = []
        for num in nums:
            if num % 2 == 0:
                total += num
        for q in queries:
            temp = nums[q[1]]
            nums[q[1]] += q[0]
            if temp % 2 == 0:
                if nums[q[1]] % 2 == 0:
                    total = total - temp + nums[q[1]]
                else:
                    total -= temp
            else:
                if nums[q[1]] % 2 == 0:
                    total += nums[q[1]] 
            result.append(total)
        return result
            