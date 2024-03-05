class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])

        # Finding the maximum for the rows
        for row in range(len(grid)):
            rows[row] = max(grid[row])
            
        # Finding the maximum for the columns
        for col in range(len(grid[0])):
            maxim = float('-inf')
            for row in range(len(grid)):
                maxim = max(maxim, grid[row][col])
            cols[col] = maxim

        # Iterate through the arrays to find the minimum and compute the result by deducting fron the numbers in the array
        result = 0
        for i in range(len(rows)):
            for j in range(len(cols)):
                minimum = min(cols[j], rows[i])
                diff =  (minimum - grid[i][j]) 
                if diff > 0:
                    result += diff 
                
        
        return result




        