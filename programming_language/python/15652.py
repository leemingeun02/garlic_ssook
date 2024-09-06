N, M = map(int, input().split())

def backtracking(n, m, string=[]):
    if len(string) == m:
        print(*string, sep=" ")
        return
    for i in range(1, n+1):
        if string and string[-1] <= i:
            backtracking(n, m, string + [i])
        elif not string:
            backtracking(n, m, string + [i])



backtracking(N, M)