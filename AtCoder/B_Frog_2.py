n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

table = [0] * n
table[-1] = 0
table[-2] = abs(nums[-2] - nums[-1])

for i in range(n - 3, -1, -1):
    val = float('inf')

    j = 1
    while j <= k and i + j < n:
        val = min(val, abs(nums[i] - nums[i + j]) + table[i + j])
        j += 1

    if val != float('inf'):
        table[i] = val

    # print(table)
print(table[0])

    
    
