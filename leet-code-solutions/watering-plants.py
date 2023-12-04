class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        orig_capacity = capacity
        ans = 0
        i = 0
        while i < len(plants):
            if plants[i] > capacity:
                ans += (2*i + 1)
                capacity = orig_capacity  
            else:
                ans += 1
            capacity -= plants[i]
            i += 1
            print(capacity, ans)
        return ans