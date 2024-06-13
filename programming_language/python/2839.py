N = int(input())

result = []
for i in range(N//3):
    for j in range(N//5):
        if 3*i + 5 * j == N:
            result.append(i+j)

if result:
    print(min(result))
else:
    print(-1)