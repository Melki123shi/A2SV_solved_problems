class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = 0
        col = 0
        result = 0
        while row < len(mat) and col < len(mat):
            result += mat[row][col]
            row += 1
            col += 1

        row = 0
        col = len(mat) - 1
        while row < len(mat) and col > -1:
            result += mat[row][col]
            row += 1
            col -= 1
        
        if len(mat) % 2 == 0:
            return result
        result -= mat[len(mat) // 2][len(mat) // 2]
        return result

