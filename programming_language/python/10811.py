N, M = map(int, input().split())

baskets = []
for a in range(N):
    baskets.append(a+1)

print(baskets)

for i in range(M):
    i, j = map(int, input().split())
    if (j-i) % 2 == 1:
        asdf = int(((j-i)/2))
        for a in range(asdf):
            baskets[i+a], baskets[j+1-a] = baskets[j+1-a], baskets[i+a]
        print(baskets, sep=' ')
    # if (j-i) % 2 == 0:
        