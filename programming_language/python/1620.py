import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = dict()
problem = set()

for i in range(1, N+1):
    pokemon[i] = input().rstrip()

for i in range(M):
    problem.add(input().rstrip())

for i in problem:
    if i.isdigit():
        print(problem[int(i)])
    else: #문자이므로 값을 통해 키값 찾아 키값 출력
        for a, b in pokemon.items():
            if b == i:
                print(a)
                break