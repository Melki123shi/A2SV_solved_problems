class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = ['' for i in range(len(indices))]

        for i,ind in enumerate(indices):
            string[ind] = s[i]
        return ''.join(string)
        
