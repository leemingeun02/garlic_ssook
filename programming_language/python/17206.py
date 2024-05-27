import sys
input = sys.stdin.readline

T = int(input())
Ns = []

Ns= list(map(int, input().split(" ")))


for i in range(T):
    sum = 0
    for j in range(Ns[i]+1):
        if j % 3 == 0 or j % 7 == 0:
            sum += j
    print(sum)


    #질문: 무엇이문제인가?