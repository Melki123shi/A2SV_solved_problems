class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k < numOnes:
            return k

        capacity = [numOnes,numOnes + numZeros, numOnes + numZeros + numNegOnes]
        vals = [1, 0 , -1]
        sums = [numOnes, numOnes , numOnes - numNegOnes]

        for i in range(3):
            if capacity[i] == k:
                return sums[i]

            if capacity[i] > k:
                return sums[i - 1] + (vals[i] * (k - capacity[i - 1]))
        return sums[-1]
        
        