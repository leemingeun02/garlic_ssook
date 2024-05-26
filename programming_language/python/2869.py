A, B, V = map(int, input().split())

answer = V // (A-B) #몫

if (V <= (answer-1) * (A - B) + A):
    print(answer)
elif  (V <= (answer) * (A - B) + A):
    print(answer+1)