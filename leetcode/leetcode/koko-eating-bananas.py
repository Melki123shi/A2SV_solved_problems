class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(speed):
            hour = 0
            for pile in piles:
                hour += ceil(pile / speed)
            
            return hour


        minimum = 1
        maximum = max(piles)

        while maximum >= minimum:
            speed = minimum + (maximum - minimum) // 2
            hour = hours(speed)
            if hour <= h:
                maximum = speed - 1
            else:
                minimum = speed + 1

        return minimum

                