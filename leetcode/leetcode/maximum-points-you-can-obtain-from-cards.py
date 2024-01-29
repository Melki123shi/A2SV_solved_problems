class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        total = sum(cardPoints)
        sub = sum(cardPoints[:window_size])
        result = total - sub

        for i in range(window_size,len(cardPoints)):
            sub = sub + cardPoints[i] - cardPoints[i - window_size]
            result = max(result, total - sub)

        return result
            
