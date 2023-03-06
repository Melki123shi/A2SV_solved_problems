class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            di = x**2 + y**2
            heapq.heappush(minHeap,(di,[x,y]))

        ans = []
        for i in range(k):
            di, h = heapq.heappop(minHeap)
            ans.append(h)
        return ans
