import sys
input = sys.stdin.readline

N = int(input())

member = {}


for _ in range(N):
    name, att = input().rstrip().split()
    member[name] = att

for key in sorted(member, reverse=True):
    if member[key] == "enter":
        print(key)