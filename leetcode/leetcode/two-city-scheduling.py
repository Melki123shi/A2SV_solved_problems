class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        LEN = len(costs)
        city1 , city2 = 0, 0
        result = 0
        costs = sorted(costs, key=lambda x : abs(x[0] - x[1]), reverse = True)
            
        i = 0
        while i < LEN and city1 < LEN//2 and city2 < LEN//2:
            if costs[i][0] < costs[i][1]:
                result += costs[i][0]
                city1 += 1
            else:
                result += costs[i][1]
                city2 += 1
            i += 1
        
        while i < LEN and city1 < LEN//2:
            result += costs[i][0]
            i += 1
        
        while i < LEN and city2 < LEN//2:
            result += costs[i][1]
            i += 1

        return result  
        