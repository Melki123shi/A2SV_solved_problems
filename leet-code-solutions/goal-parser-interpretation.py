class Solution:
    def interpret(self, command: str) -> str:
        ans = ''
        for i,string in enumerate(command):
            if (i < len(command) - 1) and command[i] == '(':
                if command[i + 1] == ')':
                    ans += 'o'
                else:
                    ans += 'al'
            elif string == 'G':
                ans += string
        return ans

        