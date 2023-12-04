class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        if start < destination:
            dist = sum(distance[start: destination])
        else:
            if destination == 0:
                dist = sum(distance[start - 1:: -1])
            else:
                dist = sum(distance[start - 1: destination - 1: -1])
        return min((total - dist), dist)