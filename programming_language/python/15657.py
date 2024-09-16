N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
                
def backtracking(answer=[]):
    if len(answer) == M:
        print(*answer)
    
    else:
        for i in num_list:
            if not answer:
                answer.append(i)
                backtracking(answer)
                answer.pop()
            elif answer[-1] <= i:
                answer.append(i)
                backtracking(answer)
                answer.pop()

backtracking()