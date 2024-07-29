import sys

input = sys.stdin.readline

def cantor(N, i = 0, string = "-"):
    if i == N:
        return string
    else:
        i += 1
        string += " "*len(string) + string
        return cantor(N, i, string)

for N in sys.stdin:
    N = int(N)
    if N >= 0 and N<= 12:
        print(cantor(N))
    else:
        break