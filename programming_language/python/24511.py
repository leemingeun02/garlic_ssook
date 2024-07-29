import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue_extract = []
for i in range(len(A)):
    if A[i] == 0:
        queue_extract.append(B[i])

# 삽입하는 수열의 원소 개수만큼 queue_extract 에서 반대로 출력
if M <= len(queue_extract):
    print(*queue_extract[-1: -M-1 : -1])

else:
    print(*(queue_extract[::-1]+ C[0: M - len(queue_extract)]))
# 남은 개수만큼 삽입하는 수열의 원소에서 순서대로 출력