T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    for i in range(len(S)):
        print(S[i] * R, end='')
    print()