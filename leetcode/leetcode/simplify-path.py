class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for char in path:
            if char == '.' or char == '':
                continue
            if not stack and char != '..':
                stack.append(char)
            elif stack and char == '..':
                stack.pop()
            elif char != '..':
                stack.append(char)

        return '/' + '/'.join(stack)


                    

