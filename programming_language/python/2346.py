import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
paper_number = list(map(int, input().split()))

index_with_number = deque((i, paper_number[i]) for i in range(len(paper_number)))


for i in range(N):
    target_number = index_with_number[0][1]


    if target_number >= 1: #양수인 경우
        print(index_with_number[0][0] + 1, end=' ')
        index_with_number.popleft()
        if index_with_number:
            for i in range(target_number-1):
                index_with_number.append(index_with_number.popleft())

    else: #음수인 경우 반대쪽으로 돌아가기
        print(index_with_number[0][0] + 1, end=" ")
        index_with_number.popleft()
        if index_with_number:
            for i in range(-target_number):
                index_with_number.appendleft(index_with_number.pop())