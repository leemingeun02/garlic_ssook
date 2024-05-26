A, B = map(int, input().split())
C = int(input())

min = B + C
add = min // 60

hour = A + add

if hour >=24:
    hour = hour - 24
min = min - (60 * add)

print(hour, min)