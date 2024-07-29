bingo_pan = []
for i in range(5):
    bingo_pan.append(list(map(int, input().split())))

sahoi = []
for i in range(5):
    sahoi.append(list(map(int, input().split())))

flag = 0

for a in range(5):
    if flag == 1:
        break
    for b in range(5):
        if flag == 1:
            break
        for c in range(5):
            if flag == 1:
                break
            if sahoi[a][b] in bingo_pan[c]:
                bingo_pan[c][bingo_pan[c].index(sahoi[a][b])] = 0
                #빙고확인과정
                #대각선확인
                bingo_number = 0

                if bingo_pan[0][0] == 0 and bingo_pan[1][1] == 0 and bingo_pan[2][2] == 0 and bingo_pan[3][3] == 0 and bingo_pan[4][4] == 0:
                    bingo_number += 1
                    if bingo_number == 3:
                            print(5*(a+1) + b+1)
                            flag = 1
                            break
                if bingo_pan[4][0] == 0 and bingo_pan[3][1] == 0 and bingo_pan[2][2] == 0 and bingo_pan[1][3] == 0 and bingo_pan[0][4] == 0:
                    bingo_number += 1
                    if bingo_number == 3:
                            print(5*(a) + b+1)
                            flag = 1
                            break
                #가로선확인
                for d in range(5):
                    if sum(bingo_pan[d]) == 0:
                        bingo_number += 1
                        if bingo_number == 3:
                            print(5*(a) + b+1)
                            flag = 1
                            break
                #세로선확인
                for d in range(5):
                    if bingo_pan[0][d] == 0 and bingo_pan[1][d] == 0 and bingo_pan[2][d] == 0 and bingo_pan[3][d] == 0 and bingo_pan[4][d] == 0:
                        bingo_number += 1
                        if bingo_number == 3:
                            print(5*(a) + b+1)
                            flag = 1
                            break 