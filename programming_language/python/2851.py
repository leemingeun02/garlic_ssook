import sys
score_list = []
sum = 0
for _ in range(10):
    A = int(sys.stdin.readline())
    score_list.append(A)

for i in range(10):
    if abs(100 - sum) < abs(100 - sum - score_list[i]):
        break
    else:
        sum = sum+score_list[i]

print(sum)

