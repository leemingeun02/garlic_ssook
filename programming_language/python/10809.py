S = input()

answer = [-1] * 26

#a부터 위치를 찾는다.
for Y in range(26):
    for X in range(len(S)):
        if chr(Y+ord('a')) == S[X]:
            answer[Y] = X
            break

print(*answer, sep=' ')