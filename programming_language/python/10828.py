import sys
input= sys.stdin.readline
stack = []

N = int(input())
command = []
for i in range(N):
    command = input().rstrip().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])
        stack.pop()
    
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])