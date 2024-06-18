import sys
input = sys.stdin.readline
N = int(input())

coordinate = {}

for i in range(N):
    x, y = map(int, input().split())
    if x not in coordinate:
        coordinate[x] = set()
    coordinate[x].add(y)


for i in sorted(coordinate):
    for j in sorted(coordinate[i]):
        print(i, j)