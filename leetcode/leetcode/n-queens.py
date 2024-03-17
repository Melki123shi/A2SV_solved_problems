class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        negDiag = set()
        posDiag = set()

        result = []
        pos = [['.'] * n for _ in range(n)]
        def backtrack(row):
            if n == row:
                return result.append([''.join(x) for x in pos])

            for col in range(n):
                if col in colSet or (row - col) in negDiag or (row + col) in posDiag:
                    continue

                colSet.add(col)
                negDiag.add(row - col)
                posDiag.add(row + col)
                pos[row][col] = 'Q'

                backtrack(row + 1)
                
                pos[row][col] = '.'
                colSet.remove(col)
                negDiag.remove(row - col)
                posDiag.remove(row + col)
        
        backtrack(0)
        return result


                

            

        

       
                    