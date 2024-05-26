N = int(input())
DC = []
for i in range(N):
    DC.append(list(map(int, input().split())))

answer = 0

for i in range(N):
    d, c = DC[i]
    for j in range(N):
        if i != j:
            if d > DC[j][0]:
                if c < DC[j][1]:       
                    if c > DC[j][1]:
                        if d < DC[j][0]:
                            answer += 1
                            break
        else:
                pass
print(answer)