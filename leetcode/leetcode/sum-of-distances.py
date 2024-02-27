class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        hash_store = {}

        for i, num in enumerate(nums):
            if num not in hash_store:
                hash_store[num] = []
            hash_store[num].append(i)
        
        #compute the prefix sum
        for key in hash_store:
            prefix_sum = 0
            val = hash_store[key]
            for i in range(1, len(val)):
                val[i] += val[i - 1]

        # iterate and return the result
        for key in hash_store:
            prefix_sum = hash_store[key]
            for i in range(len(prefix_sum)):
                if i == 0:
                    index = prefix_sum[0]
                    result[index] = (prefix_sum[-1] - prefix_sum[i] - (index*(len(prefix_sum) - i - 1)))
                else:
                    index = prefix_sum[i] - prefix_sum[i - 1]
                    if i == len(prefix_sum) - 1:
                        result[index] = (i*index) - prefix_sum[i - 1]
                    else:
                        result[index] = ((i*index) - prefix_sum[i - 1]) + (prefix_sum[-1] - prefix_sum[i] - (index*(len(prefix_sum) - i - 1)))
                    
        return result


        