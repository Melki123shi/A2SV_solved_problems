class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        result = float('-inf')
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                total = sum(grid[row][col: col + 3]) + sum(grid[row + 2][col:col + 3]) + grid[row + 1][col + 1]
                result = max(result, total)
        return result

            