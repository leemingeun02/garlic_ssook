asdf = input()
str_X = "".join(sorted(asdf))
int_X = int(str_X)

list_X = [0,0,0,0,0,0,0,0,0,0] #각 숫자별 개수(같은숫자여러개인경우의 백트래킹)
X_min = min(str_X)
for i in str_X:
    list_X[int(i)] += 1


depth = 0


def backtracking(answer=""):
    global list_X
    global depth
    if answer and len(answer) == len(str_X) and int(answer) > int(asdf):
        print(answer)
        exit()
    else:
        for i in str_X:
            if not answer or list_X[int(i)] != 0:
                list_X[int(i)] -= 1
                depth += 1
                backtracking(answer+i)
                list_X[int(i)] += 1
                depth -= 1
    if depth == 0:
        print(0)
backtracking()
