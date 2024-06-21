N, M = map(int, input().split())

data = [0] * N
for i in range(N):
    data[i] = list(map(int, input().split()))
    data[i] = min(data[i])

data2 = []

for i in range(N):
    data2.append(data[i])
data2.sort()

print(data2[-1])