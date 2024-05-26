N = int(input())

for i in range(N):
    for j in range(N-i-1):
        print(" ", end='')
    for j in range((i+1)*2 -1):
        print("*", end='')
    print()

for i in range(N-1):
    print(" " * (i+1), end='')
    print("*" * (2*(N-i)-3),end='')
    print()