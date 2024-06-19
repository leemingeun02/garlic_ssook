import sys
input = sys.stdin.readline

M, N = map(int, input().split())



racket = [1] * 1000001
racket[0] = 0
racket[1] = 0
for i in range(4, 1000001, 2):
    racket[i] = 0

for i in range(3, 1000001, 2):
    if racket[i] == 1:
        for j in range(i*2, 1000001, i):
            racket[j] = 0

for i in range(M, N+1):
    if racket[i] == 1:
        print(i)