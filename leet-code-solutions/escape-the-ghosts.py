class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        me = abs(target[0]) + abs(target[1])

        for g in ghosts:
            d = abs(target[0] - g[0]) + abs(target[1] - g[1])
            if d <= me:
                return False
        return True