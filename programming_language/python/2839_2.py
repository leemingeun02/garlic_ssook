N = int(input())

five = N // 5
result = -1
for i in range(five, -1, -1):
    rem = N - i * 5
    if rem % 3 == 0:
        result = i + rem // 3
        break

print(result)