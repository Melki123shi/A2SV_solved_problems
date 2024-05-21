n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

for row in range(1, n):
    for col in range(3):
        if col == 0:
            val = max(matrix[row - 1][col + 1], matrix[row - 1][col + 2])
        elif col == 1:
            val = max(matrix[row - 1][col - 1], matrix[row - 1][col + 1])
        else:
            val = max(matrix[row - 1][col - 1], matrix[row - 1][col - 2])

        matrix[row][col] += val
print(max(matrix[-1])) 
