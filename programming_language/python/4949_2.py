import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    stack = []
    result = 'yes'
    if s == '.':break
    for ch in s:
        if ch == "(" or ch=="[":
            stack.append(ch)
        elif ch==")":
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
        elif ch == ']':
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                result = 'no'
    if stack:
        result="no"
    

    print(result)