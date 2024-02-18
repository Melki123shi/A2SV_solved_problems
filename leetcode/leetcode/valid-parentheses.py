class Solution:
    def isValid(self, s: str) -> bool:
        openings = {'(' : 0, '[' : 1, '{' : 2}
        closing = {')' : 0, ']' : 1, '}' : 2}
        stack = []

        for st in s:
            if st in openings:
                stack.append(st)
            else:
                if not stack or openings[stack[-1]] != closing[st]:
                    return False
                stack.pop() 
        
        return not stack
