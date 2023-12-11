class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        v = len(arr)/4
        count = 1
        for i in range(len(arr) - 1):
            
            if arr[i] == arr[i + 1]:
                count += 1
            else:
                count = 1
            if count > v:
                return arr[i]
        return 0


