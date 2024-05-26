N = int(input())
score = list(map(int, input().split()))
max = max(score)

for i in range(N):
    score[i] = score[i] / max * 100

sum = 0
for i in range(N):
    sum = sum + score[i]
answer = sum/N
print(answer)
