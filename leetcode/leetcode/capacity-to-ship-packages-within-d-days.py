class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validDays(mid):
            day =  1
            current = 0

            for weight in weights:
                current += weight
                if current > mid:
                    current = weight
                    day += 1
            return day
            

        minimum = max(weights)
        maximum = sum(weights)

        while minimum <= maximum:
            mid =  minimum + (maximum - minimum) // 2
            day = validDays(mid)

            if day <= days:
                maximum = mid - 1
            else:
                minimum = mid + 1
        
        return minimum

            
                
        