from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
circle = deque(range(1, N+1))

print(numbers)

for i in range(N):
    print(circle.popleft())
    print