N = int(input())

answer = 0
integers = list(map(int, input().split(" ")))


def identify(a): ##소수인지 확인하는 함수 정의
    flag = True
    if a == 1:
        flag = False
    else:            
        for i in range(2, a-1):
            if a % i == 0:
                flag *= 0
                break
    return flag
for i in range(N):
    if identify(integers[i]) == True:
        answer += 1
print(answer)