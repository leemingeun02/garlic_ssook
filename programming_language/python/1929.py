import sys
input = sys.stdin.readline

M, N = map(int, input().split(" "))


for i in range(M, N, 1):
    yaksu_identifyer = True
    for j in range(2, i):
        if i % j == 0:
            yaksu_identifyer = False
            break
        else:
            pass
    if yaksu_identifyer == True:
        print(i)