import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

command = 0

queue = deque()
for i in range(N):
    command = list(input().split())
    if len(command) == 2:
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif command[0]=="size":
        print(len(queue))
    elif command[0]=="empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command[0]=="front":
        print(queue[0])
    elif command[0]=="back":
        print(queue[-1])