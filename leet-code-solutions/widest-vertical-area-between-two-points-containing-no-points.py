class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for pt in points:
            x.append(pt[0])
        x.sort()
        maximum = 0
        for i in range(len(x) - 1):
            maximum = max(maximum, x[i + 1] - x[i])
        return maximum

