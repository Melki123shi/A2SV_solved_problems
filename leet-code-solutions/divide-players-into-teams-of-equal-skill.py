class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        result = 0
        i = 0
        j = len(skill) - 1
        num = skill[i] + skill[j]

        while i < j:
            if skill[i] + skill[j] != num:
                return -1
            else:
                result += (skill[i] * skill[j])
                i += 1
                j -= 1
        return result
        