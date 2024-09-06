H, W = map(int, input().split())

sky = [0] * H
for i in range(H):
    sky[i] = input()


for a in range(H):
    for b in range(W):
        if sky[a][b] == "c":
            print(0, end=" ")
            continue
        else:#있는경우
            if b == 0: #비가 0이면 무조건 -1
                print(-1, end=" ")
            else: #비가 0이아닌경우 c있는지 확인후 잇으면 더해서 답제출
                answer = -1
                counter = 2
                for c in range(b-1, -1,-1):
                    if sky[a][c] == "c":
                        answer += counter
                        break
                    counter += 1
                print(answer, end= " ")
    print()
