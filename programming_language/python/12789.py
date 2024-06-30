import sys
input = sys.stdin.readline
N = int(input()) + 1
line = list(map(int, input().split()))
stack= [-1]
line += [N] + [0]*N

def problem_sort(list):
    i = 1
    result = "Nice"
    while i <=N:
        if list[0] != i:
            if stack[-1] == i:
                stack.pop()
                i += 1
            elif i in list:
                stack.append(list[0])
                del list[0]
            else:
                return "Sad"
        else:
            del list[0]
            i+= 1
    return result

print(problem_sort(line))
# 함수에 리스트가 입력된다.
#함수에 입력된 리스트에서 1부터 시작한 제일작은 숫자가 나올때까지 스택으로 옮긴다.
#리스트에서 제일 작은 숫자를 제거한다.
#다음 제일 작은 숫자를 찾는다.
#제일작은 숫자가 리스트안에 묻혀있으면 숫자가 나올때까지 스택으로 옮긴다.
#제일 작은 숫자가 스택 안에 묻혀있으면 ㅈ됏으므로 sad를 출력한다.
#리스트에서 제일 작은 숫자를 뺀다
#무한반복
#아무것도 남아있지 않으면 nice를 출력한다.

