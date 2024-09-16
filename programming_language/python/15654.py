N, M = map(int, input().split())

num_list = list(input().split())
num_list.sort()

def backtracking(answer=[]):
    if len(answer) == M:
        print(*answer, sep=" ")
    else:
        for i in num_list:
            if i not in answer:
                answer.append(i)
                backtracking(answer)
                answer.pop()
backtracking()