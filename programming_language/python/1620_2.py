import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon1 = {}
pokemon2 = {}
for i in range(1,N+1):
    monsterName = input().rstrip()
    pokemon1[i] = monsterName
    pokemon2[monsterName] = i

for _ in range(M):
    search = input().rstrip()
    if search.isdigit():
        print(pokemon1[int(search)])
    else:
        print(pokemon2[search])