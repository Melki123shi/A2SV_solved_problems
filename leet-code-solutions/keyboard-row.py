class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []

        row_1 = "qwertyuiop"
        row_2 = "asdfghjkl"
        row_3 = "zxcvbnm"

        keyboard = {}
        for i in row_1:
            keyboard[i] = 1
        for i in row_2:
            keyboard[i] = 2
        for i in row_3:
            keyboard[i] = 3
        
        for word in words:
            temp = keyboard[word[0].lower()]
            isTypeable = True
            for w in word:
                if keyboard[w.lower()] != temp:
                    isTypeable = False
                    break
            if isTypeable:
                result.append(word)

        return result