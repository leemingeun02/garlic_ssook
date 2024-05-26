import copy

score = []
sum = 0
answer = []
for i in range(8):
    score.append(int(input()))
score_dual = copy.deepcopy(score)
score.sort(reverse=True)

for i in range(5):
    sum = sum + score[i]

for i in range(8):
    if score[4] <= score_dual[i]:
        answer.append(i+1)

answer.sort()


print(sum)
print(*answer)