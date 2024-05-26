N = []
for i in range(10):
    N.append(int(input()))

rest = [0] * 10
for i in range(10):
    rest[i] = N[i] % 42   # 여기까지 맞음


answer = 10

for a in range(9):
    for b in range(a, 9, 1):
        if rest[a] == rest[b + 1]:
            answer = answer -1
            break
print(answer)

