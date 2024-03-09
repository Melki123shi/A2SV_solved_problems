class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target:
            return letters[0]


        start, end = 1, len(letters)
        while start < end:
            mid = (start + end) // 2
            if letters[mid] > target and letters[mid - 1] <= target:
                return letters[mid]

            elif letters[mid] > target:
                end = mid
            else:
                start = mid + 1
                
        return letters[0]


