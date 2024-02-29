class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(pos):
            result =''
            index = pos
            number = 0

            while index < len(s):
                if s[index].isdigit():        
                    number = number*10 + int(s[index])
                elif s[index] == '[':
                    temp, i = dfs(index + 1)
                    result += number * temp
                    index = i
                    number = 0
                
                elif s[index] == ']':
                    return result, index
                
                else:
                    result += s[index]
                index += 1
            
            return result, index

        return dfs(0)[0]

        