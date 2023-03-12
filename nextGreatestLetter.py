class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s =0 
        e = len(letters)-1
        ans = ""
        while s < e:
            m = (s+e)//2
            print(s,m,e)
            if letters[m] <= target:
                s= m
            else:
                ans = letters[m]
                if m>0 and letters[m-1] <= target:
                    return letters[m]
                e = m
            if e == s+1:
                if letters[e] > target and letters[s]>target:
                    return letters[s]
                elif letters[e] > target:
                    return letters[e]
                return letters[0]
