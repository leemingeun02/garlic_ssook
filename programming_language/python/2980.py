import sys

input = sys.stdin.readline

N, L = map(int, input().split())

time = 0
current_distance = 0

D = [-1] * 100
R = [-1] * 100
G = [-1] * 100
for i in range(N):
    D[i], R[i], G[i] = map(int, input().split())


while current_distance != L:
    if current_distance in D: #빨간불인지 그린라이트인지 판별해야함
        g = G[D.index(current_distance)]
        r = R[D.index(current_distance)]
        if 0 <=time % (g + r) < r: #빨간불일때 넘기기
            time += 1
            current_distance += 0
            continue
    time += 1
    current_distance += 1
     

print(time)