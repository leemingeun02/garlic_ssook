N = int(input())


stringggg = input()


mokpan = [["." for _ in range(N)]for _ in range(N)]


#현재좌표 설정
current_colum = 0
current_row = 0


#반복 후 
for i in range(len(stringggg)):
    if stringggg[i] == "D":
        if current_row +1 < N:
            mokpan[current_row][current_colum] += "D"
            mokpan[current_row+1][current_colum] += "D"
            current_row += 1
    elif stringggg[i] == "R":
        if current_colum +1 < N:
            mokpan[current_row][current_colum] += "R"
            mokpan[current_row][current_colum+1] += "R"
            current_colum += 1
    elif stringggg[i] == "L":
        if current_colum -1 >= 0:
            mokpan[current_row][current_colum] += "L"
            mokpan[current_row][current_colum-1] += "L"
            current_colum -= 1
    elif stringggg[i] == "U":
        if current_row - 1 >= 0:
            mokpan[current_row][current_colum] += "U"
            mokpan[current_row-1][current_colum] += "U"
            current_row -= 1

#출력문자로 바꿔주기
for i in range(N):
    for j in range(N):
        target = mokpan[i][j]
        if "D" in target or "U" in target:
            mokpan[i][j] = "|"
        if "R" in target or "L" in target:
            mokpan[i][j] = "-"
        if ("D" in target or "U" in target) and ("R" in target or "L" in target):
            mokpan[i][j] = "+"

for i in range(N):
    for j in range(N):
        print(mokpan[i][j], end="")
    print()