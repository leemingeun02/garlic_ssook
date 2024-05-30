##pypy로 풀수있는방법


# import sys

# input = sys.stdin.readline

# N = int(input())

# D = [-1] * N
# C = [-1] * N
# for i in range(N):
#     D[i], C[i] = map(int, input().split(" "))


# answer = 0
# for i in range(N):
#     candidate = 1 # i 번째로 입력받은 d, c가 후보가 되는지 판별하기
#     for j in range(N):

#         if D[i]> D[j]:
#             if C[i]<C[j]:
#                 candidate *= 1
#             else:
#                 candidate *= 0

#         if C[i] > C[j]:
#             if D[i] < D[j]:
#                 candidate *= 1
#             else:
#                 candidate *= 0
#     answer += candidate
# print(answer)





#python으로 풀 수 있는 방법
import sys
input = sys.stdin.readline

N = int(input())

D = [-1] * N
C = [-1] * N
for i in range(N):
    D[i], C[i] = map(int, input().split(" "))


D.sort()
print(D)

answer = 0

print(answer)