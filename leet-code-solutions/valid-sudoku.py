class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            sets = set()
            for col in range(9):
                if (board[row][col] in sets) and board[row][col] != '.':
                    return False
                sets.add(board[row][col])

        for col in range(9):
            sets = set()
            for row in range(9):
                if (board[row][col] in sets) and board[row][col] != '.':
                    return False
                sets.add(board[row][col])

        row = 1
        while row < len(board):
            col = 1
            while col < len(board):
                sets = set(board[row][col])
                if board[row - 1][col - 1] in sets  and board[row - 1][col - 1] != '.':
                    return False
                sets.add(board[row - 1][col - 1])

                if board[row + 1][col] in sets  and board[row + 1][col] != '.':
                    return False
                sets.add(board[row + 1][col])

                if board[row - 1][col + 1] in sets  and board[row - 1][col + 1] != '.':
                    return False
                sets.add(board[row - 1][col + 1])

                if board[row][col - 1] in sets  and board[row][col - 1] != '.':
                    return False
                sets.add(board[row][col - 1])

                if board[row][col + 1] in sets  and board[row][col + 1] != '.':
                    return False
                sets.add(board[row][col + 1])

                if board[row + 1][col - 1] in sets  and board[row + 1][col - 1] != '.':
                    return False
                sets.add(board[row + 1][col - 1])
                
                if board[row - 1][col] in sets  and board[row - 1][col] != '.':
                    return False
                sets.add(board[row - 1][col])
                
                if board[row + 1][col + 1] in sets  and board[row + 1][col + 1] != '.':
                    return False 
                sets.add(board[row + 1][col + 1])
                col += 3
            row += 3

        return True

        