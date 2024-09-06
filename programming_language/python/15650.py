N, M = map(int, input().split())


def backtracking(n,m, string=""):
    if len(string) == m:
        sorted_string = "".join(sorted(list(string)))
        if str(sorted_string) == string:
            print(*list(string), sep=" ")
        return
    for i in range(1, n+1):
        if string and str(i) not in string: #없으면 추가하기/잇으면 넘기기
            backtracking(n, m, string + str(i))
        elif not string:
            backtracking(n, m, string + str(i))
backtracking(N, M)
