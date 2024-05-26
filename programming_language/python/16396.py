import sys
N = int(sys.stdin.readline())
projected = []
answer = set()
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    projected.append([a,b])

for i in range(len(projected)):
    projected[i].sort()
    a, b = projected[i]
    answer = answer | set([i for i in range(a,b+1)])


answer = list(answer) #질문: .sort붙이면 왜안됨?
answer.sort()



#몇덩이인지 찾아서 덩이수만큼 빼줘야함
minus = 0
for i in range(len(answer)-1):
    if answer[i] == answer[i+1]-1:
        pass
    else:
        minus += 1

print(len(answer)- minus-1)