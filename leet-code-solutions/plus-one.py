class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = str(int(''.join([str(x) for x in digits])) + 1)
        digits = [int(d) for d in digit]
        return digits
        