import sys
input = sys.stdin.readline

T = int(input())
list_name = []

for i in range(T):
    list_name.append(list(map(int, input().split())))

for i in range(T):
    N = 0
    for j in range(T):
        if list_name[i][0]< list_name[j][0] and list_name[i][1] < list_name[j][1]:
            N += 1
    list_name[i].append(N)
    

for i in range(T):
    print(list_name[i][2]+1, end=" ")