class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penality = 0
        for customer in customers:
            if customer == 'Y':
                penality += 1
        
        minimum = penality
        result = 0
        for i, customer in enumerate(customers):
            if customer == 'Y':
                penality -= 1
            else:
                penality += 1
            if penality < minimum:
                result = i + 1
                minimum = penality
        
        return result
        

        