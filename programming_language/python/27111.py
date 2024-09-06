import sys
input = sys.stdin.readline

N = int(input())

log = [0] * 200001
answer = 0
for i in range(N):
    a, b= map(int, input().split())
    if log[a] == 0 and b == 0:
        answer += 1
        continue
    if log[a] == 1 and b == 1:
        answer += 1
        continue
    log[a] = b
answer += sum(log)
print(answer)