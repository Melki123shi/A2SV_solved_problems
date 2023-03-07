class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        f = 0
        l = len(arr)
        
        while f < l:
            mid= (f+l)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif  arr[mid] > arr[mid-1]:
                f = mid
            elif  arr[mid] < arr[mid-1]:
                l = mid
        return -1
