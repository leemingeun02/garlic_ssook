import math

T = int(input())

def sosu_finder(a):
    if a == 0:
        return 2
    elif a == 1:
        return 2
    else:
        while True:
            flag = 1
            for i in range(2, int(math.sqrt(a))+1):
                if a % i == 0: #이면 소수가 아니므로
                    flag = 0
                    break
            if flag == 0:
                a = a + 1
                continue
            else:
                return a

for i in range(T):
    N = int(input())
    print(sosu_finder(N))