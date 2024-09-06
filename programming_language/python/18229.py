N, M, K = map(int, input().split())


flag = 0

reach_arr = []
for i in range(N):
    reach_arr.append(list(map(int, input().split())))
    
add = [0] * N

for i in range(M): #열마다
    for j in range(N): #행마다
        add[j] += int(reach_arr[j][i])
        if flag == 0 and add[j] >= K:
            print(j+1, i+1)
            flag = 1
            break