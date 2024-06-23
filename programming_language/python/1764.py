import sys
input = sys.stdin.readline

N, M  =map(int, input().split())

not_hear = set()
not_see = set()
for i in range(N):
    not_hear.add(input().rstrip())
for i in range(M):
    not_see.add(input().rstrip())
result = []
for i in not_hear:
    if i in not_see:
        result.append(i)

result.sort()
print(len(result))
print(*result,sep="\n")