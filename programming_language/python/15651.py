N, M = map(int, input().split())


def backtracking(n,m, string=""):
    if len(string) == m:
        print(*list(string), sep=" ")
        return
    for i in range(1, n+1):
        backtracking(n, m, string + str(i))
backtracking(N, M)
