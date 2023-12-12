class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        words = []
        while i < len(s):
            temp = ''
            while i < len(s) and s[i] != ' ':
                temp += s[i]
                i += 1
            if temp != '':
                words.append(temp)
            i += 1
        words = words[::-1]
        return ' '.join(words)
        
        
