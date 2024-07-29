grimpan = [[0 for i in range(100)]for i in range(100)]

N, M = map(int, input().split())

for i in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    for i in (x1, x2+1):
        for j in (y1, y2+1):
            grimpan[i][j] += 1
answer = 0
for i in range(100):
    for j in range(100):
        if grimpan[i][j]>M:
            answer = answer + 1
print(answer)