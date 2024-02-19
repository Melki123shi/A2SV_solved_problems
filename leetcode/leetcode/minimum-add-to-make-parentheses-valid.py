class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        result = 0
        for paranthesis in s:
            if paranthesis == ')':
                if not stack:
                    result += 1
                else:
                    stack.pop()
            else:
                stack.append(paranthesis)
        
        return result + len(stack)
            