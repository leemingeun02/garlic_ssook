import sys
input = sys.stdin.readline

N = int(input())
setN = input().split()
M = int(input())

for i in input().split():
    if i in setN:
        print(1)
    else:
        print(0)