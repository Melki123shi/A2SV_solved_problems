class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            d1 = abs(points[i][0] - points[i + 1][0])
            d2 = abs(points[i][1] - points[i + 1][1])

            ans += d1 + d2 - min(d1, d2)
        return ans

