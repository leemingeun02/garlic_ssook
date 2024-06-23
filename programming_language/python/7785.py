import sys
input = sys.stdin.readline

log = dict()
N = int(input())
for i in range(N):
    A, B = map(str, input().split())
    #원래 있으면 추가, 없으면 생성
    if A in log:
        log[A].append(B)
    else:
        log[A] = list()
        log[A].append(B)
answer_list = list()
for a in log:
    if len(log[a]) %2 == 1:
        answer_list.append(a)
answer_list.sort(reverse=True)

for i in range(len(answer_list)):
    print(answer_list[i])