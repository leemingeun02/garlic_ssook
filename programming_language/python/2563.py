T = int(input())

asdf = set()
for i in range(T):
    A, B = map(int, input().split(" "))
    for i in range(A, A + 10):
        for j in range(B, B + 10):
            asdf.add((i, j))
print(len(asdf))