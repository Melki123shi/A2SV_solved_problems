str1 = input()
str2 = input()
l1, l2 = len(str1), len(str2)
dp = [[0 for i in range(l2 + 1)] for _ in range(l1 + 1)]
for i in range(l1 - 1, -1, -1):
    for j in range(l2 - 1, -1, -1):
        if str1[i] == str2[j]:
            dp[i][j] = 1 + dp[i + 1][j + 1]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])


_max = max(dp[0])
max_ind = dp[0].index(_max)
i, j = 0, 0
result = []
while i < l1 and j < l2:
    if str1[i] == str2[j]:
        result.append(str1[i])
        i += 1
        j += 1
    else:
        if dp[i + 1][j] > dp[i][j + 1]:
            i += 1
        else:
            j += 1
print(''.join(result))
