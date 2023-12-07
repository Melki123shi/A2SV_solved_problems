class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, value, greater = [], [], []
        for num in nums:
            if num == pivot:
                value.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                less.append(num)
        return less + value + greater


        