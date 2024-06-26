N, K =map(int, input().split())
global people = [1] * N
people[0] = 0

global turn = 0
def yosepus(N,K):
    print(people[turn])
    people[turn] = 0
    if True:
        yosepus(N,K)