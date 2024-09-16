N, M = map(int, input().split())

tiles = []
for i in range(N):
    tiles.append(input())

answer = 0
def hello(a, b): #a, b: 좌표
    #왼쪽에서 오른쪽으로, 위에서 아래로 탐색할것이므로
    # |인 경우 위 값 확인, - 인 경우 왼쪽 값 확인
    #왼쪽 혹은 위부터 이어져있지 않은 타일임이 확인되면 answer += 1
    global answer
    if tiles[a][b] == "|":
        if a - 1 >= 0 and tiles[a-1][b] != "|":
            answer += 1
        elif a == 0:
             answer += 1
    if tiles[a][b] == "-":
        if b - 1 >= 0 and tiles[a][b-1] != "-":
            answer += 1
        elif b == 0:
             answer += 1

for i in range(N):
      for j in range(M):
            hello(i, j)
print(answer)