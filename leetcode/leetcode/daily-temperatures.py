class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        monotinic_stack = []

        for i, temperature in enumerate(temperatures):

            if not monotinic_stack:
                monotinic_stack.append([temperature, i])

            else:
                while monotinic_stack and monotinic_stack[-1][0] < temperature:
                    value = monotinic_stack.pop()
                    index =  value[1]
                    answer[index] = i - index
                monotinic_stack.append([temperature, i])

        return answer
                

        