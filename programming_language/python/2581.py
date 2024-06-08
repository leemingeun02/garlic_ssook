import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

sum = 0
smallest = -1

for i in range(N, M+1):
    if i == 1: #1은 소수가 아니므로 거른다.
        continue
    if i == 2:
        smallest = 2
        continue
    for j in range(2, i): #i가 소수인지 판별하기 위한반복문, i는 2부터 판정가능함.
        if i % j == 0: #나누어떨어지는 소인수가 존재할 때, 즉 소수가 아닐때
            break # 반복문 탈출
        if j == i-1:
            sum += i #끝까지 반복문 탈출하지 않았을 시 소수이므로 sum 에 해당 소수값을 더하고 저장.
            if smallest < 0: #소수로 판정된 경우 smallest 는 음수가 아닐시(즉 최솟값이 저장안되었을때)
                smallest = i #최솟값 저장
if smallest == -1:
    print(smallest)
else:
    print(sum)
    print(smallest)

