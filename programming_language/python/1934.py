N = int(input())

for i in range(N):
    A, B = map(int, input().split())
    #최대공약수 구하기
    common_factor = 0
    for j in range(min(A, B), 0, -1):
        if A % j == 0 and B % j == 0:
            common_factor = j
            break
    print(int(common_factor * A //j * B //j))