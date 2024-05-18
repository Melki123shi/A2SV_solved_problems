n = int(input())
nums = list(map(int, input().split()))

table = [0] * n
table[-1] = 0
table[-2] = abs(nums[-2] - nums[-1])
for i in range(n - 3, -1, -1):
    table[i] = min(abs(nums[i] - nums[i + 1]) + table[i + 1], abs(nums[i] - nums[i + 2]) + table[i + 2])
print(table[0])

    
    
