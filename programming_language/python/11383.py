N, M = map(int, input().split())

S1 = [0] * N
S2 = [0] * N
for i in range(N):
    S1[i] = input()

for i in range(N):
    S2[i] = input()

whether = 0
for i in range(N):
    for j in range(M):
        if (S1[i][j] == S2[i][2*j]) and (S1[i][j] == S2[i][2*j+1]):
            Eyfa = "Eyfa"
        else:
            Eyfa = "Not Eyfa"
            whether = 1
            break
    if whether == 1:
        break

print(Eyfa)

# S1의 i번째 인덱스 스트링의 j번째 글짜가
# S2의 i번째 인덱스 스트링의 2*j, 2*j -1번째 글짜와 동일한지 체크.