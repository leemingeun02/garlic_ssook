A, B, V = map(int, input().split(" "))

answer = (V-B) // (A-B) - 1
if (V - (A-B)*answer) == 0:
    pass
elif (V - (A-B)*answer) - A <= 0:
    answer += 1
elif (V - (A-B)*answer) - (2*A - B) <= 0:
    answer += 2
print(answer)