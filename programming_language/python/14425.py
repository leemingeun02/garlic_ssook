import sys
input = sys.stdin.readline


N, M = map(int, input().split())
S = set()
MMM = list()
for i in range(N):#집합 s저장
    S.add(input())
    
for i in range(M):#m개의 문자열 저장
    MMM.append(input())

result = 0
for i in range(len(MMM)):
    if MMM[i] in S:
        result+=1
print(result)