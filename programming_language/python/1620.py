import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = dict()
problem = dict()

for i in range(1, N+1):
    pokemon[i] = input().rstrip()

for i in range(M):
    problem[i] = input().rstrip()

for i in problem:
    if problem[i].isdigit():
        print(pokemon[int(problem[i])])
    else: #문자이므로 값을 통해 키값 찾아 키값 출력
        for a, b in pokemon.items():
            if b == problem[i]:
                print(a)
                break