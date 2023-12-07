class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        counter = 0
        i = 0
        result = []
        while i < len(nums):
            if nums[i] == pivot:
                result.insert(counter, nums[i])
            elif nums[i] > pivot:
                result.append(nums[i])
            else:
                counter += 1
                result.insert(0, nums[i])
            i += 1

        index = result.index(pivot)
        start = index
        end = index
        while end < len(result) and result[end] == pivot:
            end += 1
        end -= 1
        result[:start] = result[:start][::-1]

        return result


        