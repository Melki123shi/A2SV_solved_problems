class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x : x[1])
        result = 1
        current = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > current:
                current = points[i][1]
                result += 1

        return result
        