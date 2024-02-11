class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * (n + 1) #preserve n + 1 seats to include the edge case

        for start, end, seats in bookings:
            prefix_sum[start - 1] += seats
            prefix_sum[end] -= seats

        answer = [prefix_sum[0]]
        for i in range(len(prefix_sum) - 2):
            answer.append(answer[i] + prefix_sum[i + 1])
        
        return answer


