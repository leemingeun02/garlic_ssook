import sys
input = sys.stdin.readline

prime_list = [1] * 1000001
prime_list[0] = 0
prime_list[1] = 0
for i in range(4, 1000001, 2):
    prime_list[i] = 0
for i in range(3, int(1000001 **0.5)+1, 2):
    if prime_list[i]:
        for j in range(i*2, 1000000+ 1, i):
            prime_list[j] = 0




T = int(input())
for i in range(T):
    answer = 0
    N = int(input())
    for i in range(N//2 + 1):
        if prime_list[i] == 1:
            if prime_list[N - i] == 1: 
                answer += 1
    print(answer)