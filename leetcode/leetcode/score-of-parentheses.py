class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                top = stack.pop()
                val = max(1, 2*top)

                stack[-1] += val

        return stack.pop()


