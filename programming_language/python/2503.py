import sys
input = sys.stdin.readline

N = int(input())
num_strike_ball = []
for i in range(N):
    num_strike_ball.append(list(map(int, input().split())))



def num_baseball(num): #숫자투입시 num_strike_ball 에입력된값을 바탕으로 스트라이크 볼 계산하는 함수
    global N
    for i in range(N):
        strike = 0
        ball = 0
        for j in range(3):#스트라이크 판별
            if str(num)[j] in str(num_strike_ball[i][0]):
                ball += 1 #스트랑이크일 수도 있으므로 스트라이크 판별하기
                if str(num)[j] == str(num_strike_ball[i][0])[j]:
                    ball -= 1
                    strike += 1
        if strike != num_strike_ball[i][1] or ball != num_strike_ball[i][2]:
            return 0
    return 1


possible_number = [i for i in range(123, 1000)]
answer = 0
for i in possible_number:# 0 부터 999까지 스트라잌 볼 을 만족하는 수를 찾아서 answer 값 구하기
    if "0" in str(i) or (str(i)[0]== str(i)[1] or str(i)[1] == str(i)[2] or str(i)[2] == str(i)[0]):
        continue #서로 다른 세자리수여야 하므로 여기서 걸러주기
    if num_baseball(i) == 1:
        answer += 1

print(answer)