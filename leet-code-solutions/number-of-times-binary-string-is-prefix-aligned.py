class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        ones = 0
        for i, flip in enumerate(flips):
            ones = max(ones, flip)
            if i + 1 == ones:
                count += 1
        return count
            
        