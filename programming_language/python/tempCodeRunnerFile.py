A, B, V = map(int, input().split(" "))

answer = (V-B) // (A-B)

print(answer)

if (V - B) - answer*(A-B) - A <= 0:
    answer += 1