N = int(input())
info = []
for i in range(N):
    info.append(list(map(int, input().split())))


answer = 0
current_homework = -1
for i in range(N):
        if current_homework == 1 and info[i][2] != [0]:
        #숫자 3개이고 current_homework 정
        # 
        의유무 상관없이 재정의
        info[i][2] -= 1
        current_homework = i
    if info[i] == [0] and current_homework != -1:
        #0이고 curent_homework 정의된경우
        info[current_homework][2] -= 1

    if current_homework == 1 and info[current_homework][2] == 0:
        answer += info[current_homework][1]
    



print(answer)