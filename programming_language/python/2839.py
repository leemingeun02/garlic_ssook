N, M = map(int, input().split(" "))
hangryeol = [0 for j in range(N)]
hangryeol2 = [0 for j in range(N)]
for i in range(N):
    hangryeol[i] = list(map(int, input().split(" ")))
for i in range(N):
    hangryeol2[i] = list(map(int, input().split(" ")))

hangryeol3 = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        hangryeol3[i][j] = hangryeol[i][j] + hangryeol2[i][j]

for i in hangryeol3:
    print(*i, sep=" ")