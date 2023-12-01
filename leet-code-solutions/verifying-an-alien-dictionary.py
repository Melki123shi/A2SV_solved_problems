class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        _dict = {}
        c = 0
        for ordr in order:
            _dict[ordr] = c
            c += 1
        
        j = 0
        while j < len(words) - 1:
            i = 0
            
            while i < min(len(words[j]), len(words[j + 1])):
                if _dict[words[j][i]] < _dict[words[j+1][i]]:
                    break
                if _dict[words[j][i]] > _dict[words[j+1][i]]:
                    return False
                i += 1
         
            if words[j][:min(len(words[j]), len(words[j + 1]))] == words[j + 1][:min(len(words[j]), len(words[j + 1]))] and len(words[j]) > len(words[j + 1]):
                return False
            j += 1

        return True

