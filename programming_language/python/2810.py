N = int(input())
string = input()
i = 0
seat_and_holder = '*'

while (i<N):
    if string[i] == 'S':
        seat_and_holder += 'S*'
        i += 1
    elif string[i] == 'L':
        seat_and_holder += 'LL*'
        i += 2 ######여기까지맞음

counter = 0

final = list(seat_and_holder)
final.pop()
final.pop()
answer = 2

while final.index("*") != ValueError: