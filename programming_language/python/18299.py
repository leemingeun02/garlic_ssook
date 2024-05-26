N, M, K = map(int, input().split())
people = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    people[i] = list(map(int, input().split()))
it_ends_now = Null
total = [0] * N
for i in range(N):
    for j in range(M):
        return1 = i+1
        return2 = j+1
        total[i] +=  people[i][j]
        if total[i] >= K:
            print(return1, return2)
            it_ends_now = False
            break
    if it_ends_now == False:
        break