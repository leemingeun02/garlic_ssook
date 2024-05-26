N, M = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i] = list(map(int, input().split()))
for i in range(N):
    B[i] = list(map(int, input().split()))

C = [[0 for i in range(N)] for j in range(M)]
for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]

print(*C[0])
print(*C[1])
print(*C[2])