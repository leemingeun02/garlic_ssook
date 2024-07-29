import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
deque1 = deque()

for i in range(N):
    command = list(input().split())
    if len(command) == 2:
        if command[0] == "1": # 1 x 인 경우
            deque1.appendleft(command[1])
        else: # 2 x 인 경우
            deque1.append(command[1])
    elif command[0] == "3":
        if deque1:
            print(deque1.popleft())
        else:
            print(-1)
    elif command[0]=="4":
        if deque1:
            print(deque1.pop())
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
        if deque1:
            print(deque1[-1])
        else:
            print(-1)