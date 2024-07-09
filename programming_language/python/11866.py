from collections import deque

yosepus = deque()
N, M = map(int, input().split())

yosepus = deque(range(1,N+1))


counter = 1
print("<",end="")
while yosepus:
    if counter % M == 0:
        counter = 1
        print(yosepus.popleft(),end="")
        if yosepus:
            print(", ",end="")
    else:
        yosepus.append(yosepus.popleft())
        counter += 1

print(">", end="")