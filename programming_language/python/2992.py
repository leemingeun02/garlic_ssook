int_X = input()
list_X = list(int_X)
# list_X.sort()
int_X = int(int_X)



def backtracking(answer=list_X[0]):
    if int(answer) >= int_X:
        print(answer)
        return
    else:
        for i in list_X:
            if i not in answer:
                backtracking(answer+i)
backtracking()