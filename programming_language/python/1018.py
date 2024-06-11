import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = [0 for i in range(N)]
for i in range(N):
    board[i] = input()

ideal_board_ver1 = ["WBWBWBWB", "BWBWBWBW"] * 4
ideal_board_ver2 = ["BWBWBWBW", "WBWBWBWB"] * 4

answer = 10000


for i in range(N-7):
    for j in range(M-7):
        result1, result2 = 0, 0
        for k in range(8):
            for l in range(8):
                if ideal_board_ver1[k][l] != board[i+k][j+l]:
                    result1 += 1
                if ideal_board_ver2[k][l] != board[i+k][j+l]:
                    result2 += 1
        answer = min(answer, result1, result2)
print(answer)