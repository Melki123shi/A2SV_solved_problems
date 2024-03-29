class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []

        for col in range(len(matrix[0])):
            rows = []
            for row in range(len(matrix)):
                rows.append(matrix[row][col])
            result.append(rows)
        
        return result
        