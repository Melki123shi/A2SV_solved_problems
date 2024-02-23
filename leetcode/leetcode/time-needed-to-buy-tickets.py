class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        tickets = deque(tickets)

        while tickets:
            val = tickets.popleft()

            if val != 1:
                tickets.append(val - 1)
            elif k == 0:
                return count + 1

            if k == 0:
                k = len(tickets) - 1
            else:
                k -= 1
            count += 1

        return count
            

            
