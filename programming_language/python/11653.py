import sys
input = sys.stdin.readline

N = int(input())

def identify(a): ##소수인지 확인하는 함수 정의
    flag = 1
    if a == 1:
        flag = 0
    else:            
        for i in range(2, a-1):
            if a % i == 0:
                flag *= 0
                break
    return flag

if N == 1:
    pass
elif identify(N) == 1:
    print(N) #소수인 경우 즉 소인수분해가 불가능한 경우 해당소수만 출력
else: #소인수분해가 가능한경우
    for i in range(2, N):
        repeat = 0
        while repeat == 0:
            if N % i == 0:
                print(i)
                N = N// i
            else:
                repeat = 1