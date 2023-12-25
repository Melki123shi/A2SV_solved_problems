class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        j = len(arr) - 1

        while i < len(arr) - 1 and j > 0 and i <= j:
            if arr[i] >= arr[i + 1] and arr[j] >= arr[j - 1]:
                if i == j:
                    return True
                else:
                    return False
            if arr[i] < arr[i + 1]:
                i += 1
            if arr[j] < arr[j - 1]:
                j -= 1
        return False
