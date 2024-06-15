N = 20001

is_prime = [1] * N
is_prime[0] = 0
is_prime[1] = 0

for i in range(4, N, 2):
    is_prime[i] == 0

prime_list = [2]

for i in range(3, int(N **0.5) + 1, 2):
    if is_prime[i]:
        for j in range(i* 2, N, i):
            is_prime[j] = 0
        
for i in range(3, N, 2):
    if is_prime[i]:
        prime_list.append(i)

print(prime_list)



T = int(input())

for _ in range(T):
    a = int(input())

    if a<3:
        print(2)
        continue
    while True:
        if a %2 ==0:
            a += 1
            continue
        
        chk = 1

        for i in prime_list:
            if i > int(a ** 0.5):
                break
            if i > int(a) == 0:
                chk = 0
                break
        if chk:
            print(a)
            break
        a += 1 