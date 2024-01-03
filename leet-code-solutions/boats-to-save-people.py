class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boat = 0

        while i <= j:
            total = people[i] + people[j]
            
            if total > limit:
                j -= 1
                boat += 1
            else:
                boat += 1
                i += 1
                j -= 1
        return boat
           
        