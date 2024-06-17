def is_prime(N):# 1부터 N까지 몇개의 소수가 존재하느지 정의하는 함수
    prime_list = [1] * (2*N + 1)
    prime_list[0]= 0
    prime_list[1] = 0
    for i in range(4, 2*N + 1, 2):
        prime_list[i] = 0
    for i in range(3, int((2*N+1)**0.5)+1, 2): #홀수동안
        if prime_list[i]:
            for j in range(i*2, 2*N + 1, i):
                prime_list[j] = 0

    for i in range(0, N+1):
        prime_list[i] = 0
    return sum(prime_list)
                

    


while True:
    N = int(input())
    if N == 0:
        break
    print(is_prime(N))