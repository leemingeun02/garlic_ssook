import sys
input = sys.stdin.readline
N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

data.sort()
print(round(sum(data)/N))
print(data[N//2])

########################
data2 = dict()

for i in data:
    if i in data2:
        data2[i] += 1
    else:
        data2[i] = 1
print(data2)
values = list(data2.keys())
values.sort()
if values[-1] != values[-2]:
    for key, value in data2.item():
        if value == values[-1]:
            print(key)
else:
    pass
    #values-1을 만족하는 key값들 중 두번째로 작은 값을 출력

#######################
print(max(data)-min(data))