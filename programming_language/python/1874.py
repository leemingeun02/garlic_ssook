import sys

input = sys.stdin.readline

N = int(input())

stack = []
counter = 1
numbers = []
answer = []
for _ in range(N):
    numbers.append(int(input()))

for i in range(N):
    
    # 스택 안에 수가 있는가? >> pop()
    if stack and numbers[i] == stack[-1]:
        stack.pop()
        answer.append("-")
    #아니면 아직 그수를 추가안했기 때문에 없는가? >>push
    elif numbers[i] > counter:
        while numbers[i] >= counter:
            stack.append(counter)
            counter += 1
            answer.append("+")
    
    #스택안에 수가 이미 pop햇거나 끄집어내느라 삭제해서 없는가? >>NO
    else:
        answer.append("NO")
# print(*answer)

if "NO" in answer:
    print("NO")
else:
    for i in range(len(answer)):
        print(answer[i])