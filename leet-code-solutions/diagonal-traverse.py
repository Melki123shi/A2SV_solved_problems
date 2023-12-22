class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        diag = False
        result = [mat[0][0]]

        while len(result) != (len(mat) * len(mat[0])):
            # if row < len(mat) and col < len(mat[0]):
                    # print(result, row, col, diag)
                    if row == 0 and diag:
                        while (row != (len(mat) - 1)) and col != 0:
                            col -= 1
                            row += 1
                            result.append(mat[row][col])
                        diag = False
                    elif col == 0 and diag:
                        while row != 0 and col != (len(mat[0]) - 1):
                            col += 1
                            row -= 1
                            result.append(mat[row][col])
                        diag = False
                    
                    elif col == len(mat[0]) - 1 and diag:
                        while row != len(mat) - 1 and col != 0:
                            col -= 1
                            row += 1
                            result.append(mat[row][col])
                        diag = False
                        
                    elif row == len(mat) - 1 and diag:
                        while col != (len(mat[0]) - 1) and row != 0:
                            col += 1
                            row -= 1
                            result.append(mat[row][col])
                        diag = False
                    
                    elif col == len(mat[0]) - 1 and row != len(mat) - 1:
                        row += 1
                        # print(row, col)
                        result.append(mat[row][col])
                        diag = True


                    elif row == len(mat) - 1 and col != len(mat[0]) - 1:
                            col += 1
                            result.append(mat[row][col])
                            diag = True

                    elif row == 0 and col != len(mat[0]) - 1:
                        col += 1
                        result.append(mat[row][col])
                        diag = True
                    
                    elif col == 0 and row != len(mat) - 1:
                        row += 1
                        result.append(mat[row][col])
                        diag = True
                    
                   
                    if col < 0:
                        col += 1
                    if row < 0:
                        row += 1
                    # print(row, col)
        return result