import sys
input = sys.stdin.readline
def goldbach(N):
    prime_list = [1] * N
    prime_list[0] = 0
    prime_list[1] = 0
    for i in range(4, N, 2):
        prime_list[i] = 0
    for i in range(3, int(N **0.5)+1, 2):
        if prime_list[i]:
            for j in range(i*2, N, i):
                prime_list[j] = 0


    answer = 0
    for i in range(N//2 +1):
        if prime_list[i] == 1:
            if prime_list[N - i] == 1:
                answer += 1
    return answer


N = int(input())
for _ in range(N):
    print(goldbach(int(input())))