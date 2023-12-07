class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ind = 0
        for sp in spaces:
            sp += ind
            s = s[:sp] + ' ' + s[sp:]
            ind += 1
        return s