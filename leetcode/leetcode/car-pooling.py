class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seats = [0] * 1002
        for numPassengers, start, end in trips:
           seats[start] += numPassengers
           seats[end] -= numPassengers

        # comupte the prefix_sum and check if their is a seat
        for index in range(1, 1002):
            seats[index] += seats[index - 1]
            if seats[index] > capacity or seats[index - 1] > capacity:
                return False
        
        return True
        
        
            


        