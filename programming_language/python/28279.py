import sys
from collections import deque

N = int(input())
deque1 = deque()
for i in range(N):
    command = list(input().split())
    if len(command) == 2:
        if deque1[0] == "1":
            deque[0] = command[1]
        else:
            deque[len(deque)] =command[1]
    elif command[0] == "3":
        if deque:
            print(deque[0])
            del deque[0]
        else:
            print(-1)
    elif command[0]=="4":
        if deque:
            print(deque[len(deque)-1])
            del deque[len(deque)-1]
        else:
            print(-1)
    elif command[0]=="5":
        print(len(deque))
    elif command[0]=="6":
        if deque:
            print(0)
        else:
            print(1)
    elif command[0]=="7":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0]=="8":
        if deque:
            print(deque[len(deque)-1])
        else:
            print(-1)