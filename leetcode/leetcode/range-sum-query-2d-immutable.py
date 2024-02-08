class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in range(len(matrix)):
            t = 0
            for col in range(len(matrix[0])):
                t += matrix[row][col]
                self.matrix[row][col] = t
        
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                self.matrix[row][col] += self.matrix[row - 1][col]

       # Get the dimensions of the original matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a new matrix with increased dimensions
        new_rows = rows + 2
        new_cols = cols + 2
        new_matrix = [[0] * new_cols for _ in range(new_rows)]

        # Copy the original matrix into the new matrix
        for i in range(rows):
            for j in range(cols):
                new_matrix[i + 1][j + 1] = matrix[i][j]

        self.matrix = new_matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2 + 1][col2 + 1] - self.matrix[row2 + 1][col1] - self.matrix[row1][col2 + 1] + self.matrix[row1][col1]


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)