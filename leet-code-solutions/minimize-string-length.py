class Solution:
    def minimizedStringLength(self, s: str) -> int:
        string = [x for x in s]
        string = set(string)
        string = list(string)

        s = ''.join(string)
        return len(s)