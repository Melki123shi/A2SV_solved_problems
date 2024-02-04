class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n+1)
        for idx in range(len(bookings)):
            start, end = bookings[idx][0], bookings[idx][1]
            res[start] += bookings[idx][2]
            if end < n:
                res[end+1] += -bookings[idx][2]
        
        for idx in range(1,n+1):
            res[idx] += res[idx-1]
        res.pop(0)
        return res
    