asdf = [[0 for i in range(9)] for j in range(9)]

for i in range(9):
    asdf[i] = list(map(int, input().split()))


max = -1
row = -1
col = -1

for i in range(9):
    for j in range(9):
        if asdf[i][j] > max:
            max = asdf[i][j]
            row = i
            col = j
print(max)
print(row+1, col+1) 