N, M = map(int, input().split())
Basket = []
for i in range(N):
    Basket.append(i+1)

for _ in range(M):
    i, j = map(int, input().split())
    k = Basket[i-1]
    Basket[i-1] = Basket[j-1]
    Basket[j-1] = k

print(*Basket, sep=' ')