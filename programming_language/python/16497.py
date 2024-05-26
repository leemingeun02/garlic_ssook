import sys
N = int(sys.stdin.readline())
B = [list(map(int, sys.stdin.readline().split(" "))) for i in range(N)]
K = int(sys.stdin.readline())   #여기까지 맞음



month = [K] * 32
for i in range(N):
    a, b = B[i]
    for j in range(a, b):
        month[j] = month[j]-1
if min(month) < 0 :
    print(0)
else:
    print(1)