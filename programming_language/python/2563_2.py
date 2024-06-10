T = int(input())

paper = [[0] * 100 for _ in range(100)]

for i in range(T):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

total = 0

for p in paper:
    total += sum(p)

print(total)