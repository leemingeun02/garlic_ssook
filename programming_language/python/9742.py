import sys

sonyeol_list = [] #순열 차곡차곡 쌓는 리스트
def backtracking(string=""):
    global a
    global b
    a = sorted(a)
    b = int(b)
    if len(string) == len(a): #스트링이 
        if len(sonyeol_list) == b:
            print(sonyeol_list[b-1])
            return
    for i in range(len(a)):
        if a[i] not in string:
            backtracking(string+a[i])


for input in sys.stdin:
    a, b = input.split()
    backtracking()