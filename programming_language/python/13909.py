#a번째 창문이 어떤 약수개수를 가지느냐에 따라 몇번 열고닫히는지가 나옴.
## 닫힌채로 시작하므로 약수가 짝수개라면 닫히고(0), 홀수개라면 열림(1)
#약수의 개수는 그 최대로 분해한후 1더해서 곱하면됨

def yaksu_number(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        return 0

    dd = 2
    result = 1
    asdf = 1
    while dd != a:
        if a % dd == 0:
            asdf += 1
            a = a / dd
        else:
            result = result * asdf
            asdf = 1
            dd += 1
    if result % 2 == 0:
        return 0
    else:
        return 1


N = int(input())

windows = [0] * (N+1)

for i in range(1, N+1):
    windows[i] = yaksu_number(i)

print(sum(windows))