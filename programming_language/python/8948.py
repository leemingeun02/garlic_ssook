N = int(input())
for i in range(N):
    OX = input()
    score = 0
    accumulation = 0
    for j in range(len(OX)):
        if OX[j] == "O":
            accumulation += 1
            score += accumulation
        else:
            accumulation = 0

        

    print(score)
