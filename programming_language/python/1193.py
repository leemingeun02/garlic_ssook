# import sys
# input = sys.stdin.readline()


N = int(input())
a = 0
b = 0

for i in range(1, N+1):
    if N -i > 0:
        N = N-i
    else:
        if i %2 == 0:
            a = N
            b = i - a + 1
            break
        else:
            a = i-N + 1
            b = i - a + 1
            break


print(f"{a}/{b}")