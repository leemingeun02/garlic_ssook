import sys.stdin.readline
input = sys.stdin.readline
N = int(input())
asdf = []
for i in range(N):
    asdf.append(int(input()))
asdf.sort()

for i in range(len(asdf)):
    print(asdf[i])