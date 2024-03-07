class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque([i for i, s in enumerate(senate) if s == 'R']), deque([i for i, s in enumerate(senate) if s == 'D'])

        curr_max = len(senate)
        while radiant and dire:
            r, d = radiant[0], dire[0]
            if r < d:
                radiant.popleft()
                dire.popleft()
                radiant.append(curr_max)
                curr_max += 1
            else:
                dire.popleft()
                radiant.popleft()
                dire.append(curr_max)
                curr_max += 1
        if radiant:
            return "Radiant"
        return "Dire"

        