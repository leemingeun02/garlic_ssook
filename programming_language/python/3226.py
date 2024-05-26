N = int(input())

calls_list = []
seconds = []

for i in range(N):
    call_info = input().replace(":", " ")
    calls_list.append(list(map(int, call_info.split(" "))))
    seconds.append((calls_list[i][0] * 3600 + calls_list[i][1] * 60, calls_list[i][2] * 60, calls_list[i][0] * 3600 + calls_list[i][1] * 60+ calls_list[i][2] * 60))
print(seconds)
answer = 0

# print()