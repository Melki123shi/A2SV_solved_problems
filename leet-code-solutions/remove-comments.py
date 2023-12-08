class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        temp = ''
        isComment = False
        for s in source:
            i = 0
            while i < len(s) - 1:  
                if not isComment and s[i] + s[i + 1] == '/*':
                    i += 1
                    isComment = True
                elif not isComment and s[i] + s[i + 1] == '//':
                    break
                elif isComment and s[i] + s[i + 1] == '*/':
                    i += 1
                    isComment = False
                elif not isComment:
                    temp += s[i]
                i += 1
            print(isComment)
            if not isComment and i == len(s) - 1 :
                print(s[i], i)
                temp += s[i]

            if not isComment and temp:
                result.append(temp)
                temp = ""
        print(temp, i)
        return result
        