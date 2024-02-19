class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'/', '*', '+', '-'}
        for char in tokens:
            if char not in operators:
                stack.append(char)
            else:
                second = stack.pop()
                stack[-1] = str(int(eval(stack[-1] + char + second)))

        return int(stack.pop())

        