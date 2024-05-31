T = int(input())

for i in range(T):
    result = input()
    hello = 0
    for i in range(len(result)):
        sum = 0
        if result[i] == "O":
            hello += 1
        else:
            hello = 0
        sum += hello
    print(sum)
            