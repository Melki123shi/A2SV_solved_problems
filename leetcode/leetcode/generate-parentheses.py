class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(opening, closing, current):
            if opening == closing == n:
                result.append(''.join(current))

            if opening < n:
                current.append('(')
                backtracking(opening + 1, closing, current)
                current.pop()
            
            if closing < opening:
                current.append(')')
                backtracking(opening, closing + 1, current)
                current.pop()

        backtracking(0, 0, [])
        return result
        
            
        

            

