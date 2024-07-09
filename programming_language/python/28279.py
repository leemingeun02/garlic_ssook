import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
deque1 = deque()

for i in range(N):
    command = list(input().split())
    if len(command) == 2:
        if deque1 and command[0] == "1":
            deque1[0] = command[1]
        elif command[0] == "1" and command[]:
            deque1.insert(0, command[1])
    elif command[0] == "3":
        if deque1:
            print(deque1[0])
            del deque1[0]
        else:
            print(-1)
    elif command[0]=="4":
        if deque1:
            print(deque1[len(deque1)-1])
            del deque1[len(deque1)-1]
        else:
            print(-1)
    elif command[0]=="5":
        print(len(deque1))
    elif command[0]=="6":
        if deque1:
            print(0)
        else:
            print(1)
    elif command[0]=="7":
        if deque1:
            print(deque1[0])
        else:
            print(-1)
    elif command[0]=="8":
        if deque:
            print(deque[len(deque)-1])
        else:
            print(-1)