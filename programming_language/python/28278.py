import sys
input = sys.stdin.readline
N = int(input().rstrip())
stack = []

for i in range(N):
    ############
    x = input().rstrip()
    if x[0] =="1":
        x = x.replace("1","",1)
        x = x.replace(" ","", 1)
        stack.append(int(x))
    elif x == "2":
        if len(stack):
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif x == "3":
        print(len(stack))
    elif x == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif x == "5":
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)