class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            sets = set()
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if (row, col) in sets:
                        continue
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                    sets.add((col, row))

        transpose(matrix)
        sets = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row, col)in sets:
                    continue
                matrix[row][col], matrix[row][len(matrix[0]) - 1 - col] = matrix[row][len(matrix[0]) - 1 - col], matrix[row][col]
                sets.add((row, len(matrix[0]) - 1 - col))
        
    
