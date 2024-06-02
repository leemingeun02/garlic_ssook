T = int(input())

for i in range(T):
    H, W, N = map(int, input().split(" "))
    #짧은게 우선, 같은층이면 아래층이 우선.
    hotel = [[((i+1) * 100 + j+1) for i in range(H)]for j in range(W)]
    # print(*hotel)
    a = (N-1) // H
    b = (N-1) % H
    print(a, b)
    print(hotel[a][b])