class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False
            if i < len(name) - 1 and name[i] != name[i + 1]:
                while j < len(typed) and typed[j] == name[i]:
                    j += 1
            else:
                j += 1
            i += 1
        return ((i == len(name)) and (j == len(typed) or (j < len(typed) and set(typed[j:]) == {name[-1]})))