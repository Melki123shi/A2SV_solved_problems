class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        i = 0
        for a2 in arr2:
            arr1[i: i + count[a2]] = [a2 for _ in range(count[a2])]
            i += count[a2]
            del count[a2]
        temp = []  
        for key in count:
            temp += [key for _ in range(count[key])]

        temp.sort()
        arr1[i:] = temp
        return arr1
            


        