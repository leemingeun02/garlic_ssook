N = int(input())

answer = 0
if N == 1:
    answer = 1
else:
    while N > 1:
        N = N - 6 * answer
        answer = answer + 1
        

print(answer)