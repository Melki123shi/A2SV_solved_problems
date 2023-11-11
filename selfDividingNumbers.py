class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            st = str(i)
            isDriv = True
            for s in st:
                if s == '0' or i % int(s) != 0:
                    isDriv = False
                    break
            if isDriv:
                ans.append(i)
        return ans

                 
