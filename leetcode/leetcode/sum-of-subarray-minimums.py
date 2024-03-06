class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        monotonic_stack = []
        MOD = 10**9 + 7 
        result = 0

        for i, value in enumerate(arr):
            while monotonic_stack and arr[monotonic_stack[-1]] >= value:  
                monotonic_stack.pop()  
            if monotonic_stack:
                left[i] = monotonic_stack[-1]  
            monotonic_stack.append(i) 

        monotonic_stack = [] 

        
        for i in range(n - 1, -1, -1):  
            while monotonic_stack and arr[monotonic_stack[-1]] > arr[i]: 
                monotonic_stack.pop()  
            if monotonic_stack:
                right[i] = monotonic_stack[-1]  
            monotonic_stack.append(i) 

        for i, value in enumerate(arr):
            result += ((i - left[i]) * (right[i] - i) * value)
      
        return result % MOD