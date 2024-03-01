from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    num = [int(x) for x in input()]
    hash_map = defaultdict(lambda : 0)
    hash_map[0] += 1
    result = 0

    for i in range(n):
        num[i] -= 1

    #Compute the prefix sum
    for i in range(1, n):
        num[i] += num[i - 1]

    for i in range(n):
        result += hash_map[num[i]]
        hash_map[num[i]] += 1
    
    print(result)
