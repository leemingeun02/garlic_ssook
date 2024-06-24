import sys
input = sys.stdin.readline
N, M = map(int, input().split())

pokemon1 = {}
pokemon2 = {}

for i in range(1, N+1):
    name = input().rstrip()
    pokemon1[name] = i
    pokemon2[i] = name
for _ in range(M):
    problem = input().rstrip()

    if problem.isdigit():
        print(pokemon2[int(problem)])
    else:
        print(pokemon1[problem])