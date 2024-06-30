import sys
input = sys.stdin.readline

N = int(input())

command = []
queue = []
for i in range(N):
    command = input().rstrip().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])
        del queue[0]
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[-1])