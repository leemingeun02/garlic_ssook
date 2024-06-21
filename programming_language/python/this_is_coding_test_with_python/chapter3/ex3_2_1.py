#큰수의 법칙 문제

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

result = 0
K_comparison = 1
for i in range(M):
    if K_comparison <= K:
        K_comparison += 1
        result += numbers[0]
    else:
        K_comparison = 1
        result += numbers[1]
print(result)