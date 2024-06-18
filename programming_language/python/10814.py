import sys

input = sys.stdin.readline

N = int(input())
members = [[0,i,0]for i in range(N)]

for i in range(N):
    members[i][0], members[i][2] = map(str, input().split()) #나이와 이름을 i번째 인덱스의 0, 1번째 인덱스에 저장 >>i는 자연스레 가입번호가 됨
    members[i][0] = int(members[i][0])
members.sort()
for i in range(N):
    print(members[i][0], members[i][2])