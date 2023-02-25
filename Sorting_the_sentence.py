class Solution:
    def sortSentence(self, s: str) -> str:
            st = ""
            lst = s.split()
            lst2 = []
            for i in lst:
                lst2.append(int(i[-1]))
            lst2.sort()
            num =0
            for num in lst2:
                for i in lst:
                    if num == int(i[-1]):
                        i = i.rstrip(i[-1])
                        st += i + " " 
                num+=1
            st= st.rstrip(st[-1])
            return st
        
