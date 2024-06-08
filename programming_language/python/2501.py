N, K = map(int, input().split(" "))
yaksu_list = []
for i in range(1, N+1):
    if N % i == 0:
        yaksu_list.append(i)

if K > len(yaksu_list):
    print(0)
else:
    print(yaksu_list[K-1])