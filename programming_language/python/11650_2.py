N = int(input())
coordinate = set()
for i in range(N):
    a, b = map(int, input().split())
    coordinate.add((b,a))

asdf = list(coordinate)

asdf.sort()

for i in range(N):
    print(asdf[i][1], asdf[i][0])