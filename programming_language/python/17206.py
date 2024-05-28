import sys
input = sys.stdin.readline

# T = int(input())
# Ns = []

# Ns= list(map(int, input().split(" ")))


# for i in range(T):
#     sum = 0
#     for j in range(Ns[i]+1):
#         if j % 3 == 0 or j % 7 == 0:
#             sum += j
#     print(sum)


#     질문: 무엇이문제인가?




T = int(input())
Ns = []

Ns= list(map(int, input().split(" ")))

for i in range(T):
    sum3 = (Ns[i] // 3)*(Ns[i] // 3 + 1) *3 / 2
    sum7 = (Ns[i] // 7)*(Ns[i] // 7 + 1) * 7 / 2
    sum21 = (Ns[i] // 21 + 1)*(Ns[i] // 21) *21 / 2
    print(int(sum3 + sum7 - sum21))
