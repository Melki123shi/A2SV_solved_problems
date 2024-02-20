class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        ones = 0

        for nums in s:
            if nums == '0':
                result += ones
            else:
                ones += 1
        
        return result


            
            
        