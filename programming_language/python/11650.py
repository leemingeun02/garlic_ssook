N = int((input()))

coordinate = []

for i in range(N):
    coordinate.append(list(map(int, input().split(" "))))

coordinate.sort()

for i in range(N):
    print(*coordinate[i])