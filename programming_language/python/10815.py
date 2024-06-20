N = int(input())
card1 =list(map(int, input().split()))
card1.sort()
M = int(input())
card2 = list(map(int, input().split()))
card2.sort()


for i in range(N):
    for j in range(M):