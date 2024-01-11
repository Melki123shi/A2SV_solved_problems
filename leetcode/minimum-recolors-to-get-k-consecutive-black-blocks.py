class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        white = 0
        l = 0
        for r in range(k):
            if blocks[r] == 'W':
                white += 1
        min_white = white
        for r in range(k,len(blocks)):
            if blocks[l] == 'W':
                white -= 1
            if blocks[r] == 'W':
                white += 1
            min_white = min(min_white, white)
            l += 1
        return min_white