class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] == num[i + 1]:
                ans = max(ans, num[i - 1] + num[i] + num[i + 1]) 
        return ans
        