import sys
input = sys.stdin.readline

N = int(input())

line = list(map(int, input().split()))

stack = []
no = 1

for number in line:
    if number == no:
        no += 1

        while stack and stack[-1] == no:
            no += 1
            stack.pop()
    else:
        stack.append(number)

if stack:
    print("Sad")
else:
    print("Nice")