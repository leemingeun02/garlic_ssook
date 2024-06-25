import sys
input = sys.stdin.readline

K = int(input().rstrip())

stack = []
for i in range(K):
    N = int(input().rstrip())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))