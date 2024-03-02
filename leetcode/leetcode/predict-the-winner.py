class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
    
        def minimax(start, end, score, max_player):
            if start > end:
                return score >= 0
            
            if max_player:
                left = minimax(start = start + 1, end = end, score = score + nums[start], max_player = False)
                if left:
                    return left

                right = minimax(start = start, end = end - 1, score = score + nums[end], max_player = False) 
                return left or right

            else:
                left = minimax(start = start + 1, end = end, score = score - nums[start], max_player = True)
                if not left:
                    return left
                    
                right = minimax(start = start, end = end - 1, score = score - nums[end], max_player = True) 
                return left and right
        
        score = 0
        start = 0
        end = len(nums) - 1
        max_player = True
        return  minimax(start, end, score, max_player)