import math

N, kim_num, lim_num = map(int, input().split())

answer = 0
current_num = 0
while True:
    if abs(kim_num - lim_num) == 1 and abs(kim_num//2 - lim_num//2) == 1: ##같은 라운드일때(1,2)(3,4)(5,6)....
        print(answer+1) #프린트하고 반복문 탈출
        break
    # elif 0: #서로 대결하지 않는지 확인하는 절차
    else: #반띵시키고 다음라운드로 넘어가는 절차
        answer += 1
        N = math.ceil(N/2)
        kim_num = math.ceil(kim_num/2)##1, 2 중 하나라면 다음번에는 1이 되어야함>>math.ceil사용
        lim_num = math.ceil(lim_num/2)
        # print(N, answer, kim_num, lim_num)
