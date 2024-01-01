class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            ind = arr.index(max(arr[:len(arr)-i]))
            arr[:ind + 1] = arr[:ind + 1][::-1]
            arr[:len(arr) - i] = arr[:len(arr) - i][::-1]
            result.append(ind + 1)
            result.append(len(arr) - i)
        return result
        