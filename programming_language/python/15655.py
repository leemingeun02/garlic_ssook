N, M = map(int, input().split())

num_list = list(input().split())
num_list.sort()

def backtracking(answer=[]):
    if len(answer) == M:
        print(*answer, sep=" ")
    else:
        for i in num_list:
            if not answer:
                answer.append(i)
                backtracking(answer)
                answer.pop()
            elif i not in answer and i > answer[-1]:
                answer.append(i)
                backtracking(answer)
                answer.pop()
backtracking()