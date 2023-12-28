class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        obs = set([(g[0], g[1]) for g in guards]) | set([(w[0], w[1]) for w in walls])
        visited = set()

        for i, grid in enumerate(guards):
            row, col = grid
            row -= 1
            while row > -1:
                if (row, col) in obs:
                    break
                visited.add((row, col))
                row -= 1
                
            row, col = grid
            col -= 1
            while col > -1:
                if (row, col) in obs:
                    break
                visited.add((row, col))
                col -= 1

            row, col = grid
            row += 1
            while row < m:
                if (row, col) in obs:
                    break
                visited.add((row, col))
                row += 1

            row, col = grid
            col += 1
            while col < n:
                if (row, col) in obs:
                    break
                visited.add((row, col))
                col += 1

        return (m*n) - len(obs | visited)
                
                