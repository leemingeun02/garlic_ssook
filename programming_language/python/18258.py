import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

command = 0

queue = deque()
for i in range(N):
    command = list(input().split())
    command0 = command[0]
    if len(command) == 2:
        queue.append(int(command[1]))
    elif command0 == "pop":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif command0=="size":
        print(len(queue))
    elif command0=="empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command0=="front":
        if not queue:
            print(-1)
            continue
        print(queue[0])
    elif command0=="back":
        if not queue:
            print(-1)
            continue
        print(queue[-1])