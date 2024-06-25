##코드 복기/복습용
import sys
input = sys.stdin.readline
N = int(input())
member = {}

for i in range(N):
    name, ett = input().split()
    member[name] = ett







# answer_list=[]

# for k, v in log.items():
#     if v == "enter":
#         answer_list.append(k)

# answer_list.sort(reverse=True)

# for i in answer_list:
#     print(i)

#아래는 같은 내용이지만 더 짧은 코드이다.

for key in sorted(member, reverse=True):
    if member[key] == "enter":
        print(key)


