import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    pass
elif: #소수인 경우 즉 소인수분해가 불가능한 경우
else: #소인수분해가 가능한경우
    for i in range(2, N):
        repeat = 0
        while repeat == 0:
            if N % i == 0:
                print(i)
                N = N// i
            else:
                repeat = 1