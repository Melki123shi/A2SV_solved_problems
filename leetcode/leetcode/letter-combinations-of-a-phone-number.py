class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combination = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        result = []
        def backtracking(current , index):
            if len(current) == len(digits):
                return result.append(current)

            digit = combination[digits[index]]
            for char in digit:
                backtracking(current + char, index + 1)

        if len(digits) == 0:
            return []

        backtracking("", 0)
        return result
                
