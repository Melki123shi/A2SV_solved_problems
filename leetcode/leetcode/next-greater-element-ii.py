class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        LENGTH = len(nums)
        maximum = max(nums)
        answer = [0] * LENGTH
        monotonic_stack = []

        for i, num in enumerate(nums):
            if num == maximum:
                answer[i] = -1

            if not monotonic_stack:
                monotonic_stack.append([num, i])
            
            else:
                while monotonic_stack and monotonic_stack[-1][0] < num:
                    value = monotonic_stack.pop()
                    index = value[1]
                    answer[index] = num
                monotonic_stack.append([num, i])

        for i, num in enumerate(nums):
            while monotonic_stack and monotonic_stack[-1][0] < num:
                value = monotonic_stack.pop()
                index = value[1]
                answer[index] = num

        return answer
        


        