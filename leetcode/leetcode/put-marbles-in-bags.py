class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == k or k == 1:
            return 0
        
        marbles = [weights[i - 1] + weights[i] for i in range(1, len(weights))]
        marbles.sort()
        return sum(marbles[-k+1:]) - sum(marbles[:k-1])

        
        
        