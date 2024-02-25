class Solution:
    def numberOfWays(self, s: str) -> int:
        LENGTH = len(s)
        zeros = [0] * LENGTH
        ones = [0] * LENGTH

        for i, char in enumerate(s):
            if char == '0':
                zeros[i] = 1
            else:
                ones[i] = 1
        

        for i in range(1, LENGTH):
            zeros[i] += zeros[i - 1]
            ones[i] += ones[i - 1]
        
        mid_ones = 0
        mid_zeros = 0
        result = 0

        for i, char in enumerate(s):
            if char == '0':
                minimum = min(ones[i], ones[-1] - ones[i])
                if minimum != 0:
                    result += ones[i] * (ones[-1] - ones[i])
            else:
                minimum = min(zeros[i], zeros[-1] - zeros[i])
                if minimum != 0:
                    result += zeros[i] * (zeros[-1] - zeros[i])
        
        return result





        