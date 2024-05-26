N, R, C = map(int, input().split())

farm = [['.' for j in range(N)] for i in range(N)]

if ((R-1) %2 == 0 and (C-1)%2==0) or ((R-1)%2 == 1 and (C-1)%2 == 1):
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            farm[i][j] = 'v'
    for i in range(1, N, 2):
        for j in range(1, N, 2):
            farm[i][j] = 'v'

if ((R-1)%2 == 0 and (C-1)%2==1) or ((R-1)%2 == 1 and (C-1)%2 == 0):
    for i in range(0, N, 2):
        for j in range(1, N, 2):
            farm[i][j] = 'v'
    for i in range(1, N, 2):
        for j in range(0, N, 2):
            farm[i][j] = 'v'
for i in range(N):
    print(*farm[i], sep='')